#!/usr/bin/env python
"""Pool the per-repository eval runs into the paper's headline significance tests.

Each `run_eval.py` invocation writes one `raw.json` per repository and a
`scoreboard.md` whose Wilcoxon test covers that repository's 5 tasks alone. With
n=5 pairs the test is under-powered by construction (`stats.wilcoxon_signed_rank`
flags n<6), so no single scoreboard can carry the paper's claim. The claim is
pooled: 4 repositories x 5 tasks = 20 paired observations, which is the number
reported in the abstract. This script is what regenerates it, so a reader can
check the headline p-value against the committed run data rather than taking it
on trust.

Pairing rule: one pair per (repo, task) — the mean total_tokens over that cell's
runs BEFORE vs the mean AFTER. Averaging within a cell before pairing is
deliberate; the three runs of a task are repeat measurements of one condition,
not three independent observations, and treating them as 60 pairs would inflate
significance.

`total_tokens` matches TaskResult.total_tokens exactly (input + output +
cache_creation; cache-read is reported separately and never netted out).

Both model tiers are pooled the same way, so the paper's two headline numbers and
its tier comparison (Table 5) all come out of one script and cannot drift apart.
Note that Table 5's side-by-side column is a mean of per-task deltas, matching the
abstract and Table 3; a mean of the four per-repository deltas gives a slightly
different figure (-24% rather than -27%) and mixing the two in one paper invites
the reader to wonder which is real.

Usage:
    PYTHONPATH=src python eval/pool_stats.py
    PYTHONPATH=src python eval/pool_stats.py --out paper/pooled-stats.md
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from beacon.eval.stats import WilcoxonResult, wilcoxon_signed_rank  # noqa: E402

RESULTS_DIR = Path(__file__).resolve().parent / "results"

# The query-protocol runs behind Tables 3 and 5, in the paper's order.
#
# gson is the asymmetric entry at both tiers: its `*-mcp-*` directory holds only
# AFTER records, because the baseline was reused from the paired read-protocol run
# rather than re-measured. That reuse is disclosed in the paper's Threats to
# Validity and in ARTIFACT.md; encoding it here keeps the script honest about
# where each number comes from instead of silently dropping the repository.
Corpus = list[tuple[str, str, str, str]]  # (label, language, after_dir, before_dir)

TIERS: list[tuple[str, str, Corpus]] = [
    ("cost-efficient", "claude-haiku-4-5", [
        ("gson", "Java", "gson-mcp-runs3", "gson-runs3"),
        ("fmt", "C++", "fmt-mcp-runs3", "fmt-mcp-runs3"),
        ("requests", "Python", "requests-mcp-runs3", "requests-mcp-runs3"),
        ("cobra", "Go", "cobra-mcp-runs3", "cobra-mcp-runs3"),
    ]),
    ("strong", "claude-sonnet-5", [
        ("gson", "Java", "gson-sonnet-mcp-runs3", "gson-sonnet-read-runs3"),
        ("fmt", "C++", "fmt-sonnet-mcp-runs3", "fmt-sonnet-mcp-runs3"),
        ("requests", "Python", "requests-sonnet-mcp-runs3", "requests-sonnet-mcp-runs3"),
        ("cobra", "Go", "cobra-sonnet-mcp-runs3", "cobra-sonnet-mcp-runs3"),
    ]),
]


@dataclass(frozen=True)
class Pair:
    repo: str
    task_id: str
    before: float
    after: float

    @property
    def delta_pct(self) -> float:
        return (self.after - self.before) / self.before if self.before else 0.0


def _total_tokens(rec: dict) -> int:
    return (
        rec.get("input_tokens", 0)
        + rec.get("output_tokens", 0)
        + rec.get("cache_creation_input_tokens", 0)
    )


def _cell_means(raw_path: Path, mode: str) -> dict[str, float]:
    """Mean total_tokens per task_id for one mode, skipping errored runs."""
    records = json.loads(raw_path.read_text(encoding="utf-8"))
    buckets: dict[str, list[int]] = {}
    for rec in records:
        if rec.get("mode") != mode or rec.get("is_error"):
            continue
        buckets.setdefault(rec["task_id"], []).append(_total_tokens(rec))
    return {t: statistics.fmean(v) for t, v in sorted(buckets.items()) if v}


def collect_pairs(
    repos: list[tuple[str, str, str, str]], results_dir: Path
) -> tuple[list[Pair], list[str]]:
    """Build one BEFORE/AFTER pair per (repo, task). Returns (pairs, warnings)."""
    pairs: list[Pair] = []
    warnings: list[str] = []
    for label, _lang, after_dir, before_dir in repos:
        after_raw = results_dir / after_dir / "raw.json"
        before_raw = results_dir / before_dir / "raw.json"
        for path in (after_raw, before_raw):
            if not path.exists():
                warnings.append(f"{label}: missing {path.relative_to(results_dir.parent)}")
        if not after_raw.exists() or not before_raw.exists():
            continue
        after = _cell_means(after_raw, "after")
        before = _cell_means(before_raw, "before")
        for task_id in sorted(set(before) & set(after)):
            pairs.append(Pair(label, task_id, before[task_id], after[task_id]))
        for task_id in sorted(set(before) ^ set(after)):
            warnings.append(f"{label}: task {task_id} unpaired (present in only one mode)")
    return pairs, warnings


@dataclass(frozen=True)
class TierResult:
    name: str
    model: str
    corpus: Corpus
    pairs: list[Pair]
    warnings: list[str]

    def repo_pairs(self, label: str) -> list[Pair]:
        return [p for p in self.pairs if p.repo == label]

    @property
    def stats(self) -> tuple[float, float, int, WilcoxonResult]:
        deltas = [p.delta_pct for p in self.pairs]
        improved = sum(1 for p in self.pairs if p.after < p.before)
        w = wilcoxon_signed_rank([p.before for p in self.pairs],
                                 [p.after for p in self.pairs])
        return statistics.fmean(deltas), statistics.median(deltas), improved, w


def _repo_delta(tier: TierResult, label: str) -> str:
    """Mean AFTER over mean BEFORE for one repository, as a signed percentage."""
    rp = tier.repo_pairs(label)
    if not rp:
        return "n/a"
    b = statistics.fmean(p.before for p in rp)
    a = statistics.fmean(p.after for p in rp)
    return f"{(a - b) / b:+.0%}"


def _repo_table(tier: TierResult) -> list[str]:
    out = ["| Repository | Language | Before | After | Δ | Improved |",
           "|---|---|--:|--:|--:|:--:|"]
    for label, lang, _a, _b in tier.corpus:
        rp = tier.repo_pairs(label)
        if not rp:
            continue
        b, a = statistics.fmean(p.before for p in rp), statistics.fmean(p.after for p in rp)
        improved = sum(1 for p in rp if p.after < p.before)
        out.append(f"| {label} | {lang} | {b:,.0f} | {a:,.0f} | {(a - b) / b:+.0%} "
                   f"| {improved}/{len(rp)} |")
    return out


def _pooled_lines(tier: TierResult) -> list[str]:
    mean, median, improved, w = tier.stats
    out = [f"- Paired observations: **{len(tier.pairs)}** (one per repository-task cell)",
           f"- Tasks improved: **{improved}/{len(tier.pairs)}**",
           f"- Mean per-task change: **{mean:+.0%}**",
           f"- Median per-task change: **{median:+.0%}**",
           f"- Paired Wilcoxon signed-rank: **W = {w.statistic:.1f}, "
           f"p = {w.p_value:.4f}**, n = {w.n}"]
    if w.underpowered:
        out.append("- WARNING: under-powered (n < 6), treat as directional.")
    return out


def render(tiers: list[TierResult]) -> str:
    out: list[str] = ["# Pooled statistics across the query-protocol runs", ""]

    for tier in tiers:
        out += [f"## {tier.name} tier ({tier.model})", ""]
        out += _repo_table(tier)
        out += ["", "Pooled across all tasks:", ""] + _pooled_lines(tier) + [""]

    # Table 5: both tiers side by side.
    #
    # There are two defensible ways to reduce a repository to one delta, and they
    # do not agree: the ratio of its mean AFTER to its mean BEFORE (what the
    # per-repository tables above and the paper's Tables 3 and 5 report), or the
    # mean of its per-task deltas (what the significance test pairs over). On the
    # cost-efficient tier the first gives gson -23% and the second -29%.
    #
    # So this table reuses _repo_deltas, identical to the tables above, and the
    # per-task pooled figure is stated below as its own labelled line rather than
    # as a table row that would read like the same kind of number. Two clearly
    # named aggregations, never a third.
    if len(tiers) > 1:
        names = " | ".join(f"Δ {t.name}" for t in tiers)
        out += ["## Tier comparison (paper Table 5)", "",
                f"| Repository | Language | {names} |",
                "|---|---|" + "--:|" * len(tiers)]
        for label, lang, _a, _b in tiers[0].corpus:
            cells = [_repo_delta(t, label) for t in tiers]
            out.append(f"| {label} | {lang} | " + " | ".join(cells) + " |")
        out += ["", "Cells are mean AFTER over mean BEFORE per repository, the same "
                    "aggregation as the tables above.", ""]
        for t in tiers:
            mean, _median, improved, w = t.stats
            out.append(f"- Pooled over all {len(t.pairs)} tasks, {t.name} tier: "
                       f"**{mean:+.0%}** mean per-task change, {improved}/{len(t.pairs)} "
                       f"improved, p = {w.p_value:.4f}")
        out.append("")

    for tier in tiers:
        out += [f"## Per task, {tier.name} tier", "",
                "| Repository | Task | Before | After | Δ |", "|---|---|--:|--:|--:|"]
        out += [f"| {p.repo} | {p.task_id} | {p.before:,.0f} | {p.after:,.0f} "
                f"| {p.delta_pct:+.0%} |" for p in tier.pairs]
        out.append("")

    flagged = [(t.name, m) for t in tiers for m in t.warnings]
    if flagged:
        out += ["## Warnings", ""] + [f"- [{name}] {msg}" for name, msg in flagged] + [""]

    out += ["_Regenerate: `PYTHONPATH=src python eval/pool_stats.py`_"]
    return "\n".join(out) + "\n"


def main() -> int:
    # The tables use the delta sign; a cp1252 Windows console raises without this.
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--results-dir", type=Path, default=RESULTS_DIR)
    ap.add_argument("--out", type=Path, help="write markdown here instead of stdout")
    ap.add_argument("--tier", action="append", choices=[n for n, _m, _c in TIERS],
                    help="restrict to one tier (repeatable); default is every tier")
    args = ap.parse_args()

    wanted = args.tier or [n for n, _m, _c in TIERS]
    tiers: list[TierResult] = []
    for name, model, corpus in TIERS:
        if name not in wanted:
            continue
        pairs, warnings = collect_pairs(corpus, args.results_dir)
        if pairs:
            tiers.append(TierResult(name, model, corpus, pairs, warnings))
        else:
            print(f"No paired results for the {name} tier.", file=sys.stderr)
            for msg in warnings:
                print(f"  {msg}", file=sys.stderr)

    if not tiers:
        return 1

    md = render(tiers)
    if args.out:
        args.out.write_text(md, encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    else:
        sys.stdout.write(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
