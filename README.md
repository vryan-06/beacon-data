# Evaluation data: "Query, Don't Read"

Raw run data, pinned corpus, and pre-registered tasks behind every number in the
paper *Query, Don't Read: When a Repository Context Layer Saves an AI Agent Tokens,
and When It Doesn't*.

## Headline

Reading a generated repository context layer into an AI coding agent's context is
token neutral. Querying the same index through lookup tools cuts agent tokens by a
mean of 27% per task on a cost-efficient model tier (18/20 tasks improved, paired
Wilcoxon p = 0.0003), with correctness preserved. Repeating the query protocol on a
stronger tier gives a mean of -1% over the same 20 tasks (11/20, p = 0.5628),
because the stronger model already explores the bare repository efficiently.

## Regenerating the reported numbers

```
PYTHONPATH=src python eval/pool_stats.py
```

Standard library only, no network, no model, byte-identical across runs. It prints
per-repository tables and a pooled significance test for both model tiers, plus the
tier comparison that is Table 5 in the paper. `--tier cost-efficient` or
`--tier strong` restricts it; `--out FILE` writes markdown.

Each per-repository `scoreboard.md` covers only that repository's five tasks, which
is under-powered by construction, so the pooled test above is what the paper's
significance claims rest on.

## What reproduces exactly, and what does not

- **Exactly:** everything in this archive, and the aggregation over it. The pooled
  statistics are deterministic given these files.
- **Not exactly:** the agent-loop measurements themselves. The evaluation drives a
  real multi-turn coding agent whose sampling is non-deterministic, and hosted
  models change over time, so a fresh run will not reproduce these token counts. It
  should reproduce the direction and rough magnitude. That is why the raw records
  and full agent transcripts are archived here rather than only the summary.

## Layout

```
eval/results/<run>/raw.json        per-run token, turn, verdict and edit records
eval/results/<run>/scoreboard.md   that run's aggregated table
eval/results/<run>/transcripts/    full agent transcripts, one per task and mode
eval/corpus.json                   corpus with pinned commit hashes
eval/tasks/<repo>.json             five pre-registered tasks per repo, with answer keys
eval/pool_stats.py                 regenerates the pooled result and the tier comparison
src/beacon/eval/stats.py           the confidence-interval and Wilcoxon implementations
```

Run directories without `-sonnet-` are the cost-efficient tier (Claude Haiku 4.5);
`-sonnet-` directories are the strong tier (Claude Sonnet). `gson-runs3` is the
read protocol; `*-mcp-*` are the query protocol.

Two runs share a baseline rather than re-measuring it, at both tiers: see
`eval/results/gson-mcp-runs3/NOTE.md` and
`eval/results/gson-sonnet-mcp-runs3/README.md`. The paper discloses this in Threats
to Validity, and `pool_stats.py` encodes the pairing explicitly.

## Corpus (pinned commits)

| Repository | Language | Commit |
|---|---|---|
| gson (google/gson) | Java | dae37cf0fe12235b76fb09f01118a0a8c8823f42 |
| fmt (fmtlib/fmt, tag 11.0.2) | C++ | 0c9fce2ffefecfdce794e1859584e25877b7b592 |
| requests (psf/requests) | Python | 8f8b212de8c2129d7954c6cd373762880375620a |
| cobra (spf13/cobra) | Go | adbc8813901bba65827259daa8e22ff94ec1f30e |
| magic_enum (Neargye/magic_enum) | C++ | 591b64351ea8442f8b8fa044ff335d6943e8e6e0 |

The corpus repositories are not vendored here; only their commit identity is pinned.

## Scope of this archive

This is the **evaluation data**, not the tool. The tool that generates the context
layer is described in the paper and is not included in this deposit. The data here
is sufficient to check every reported number, since the numbers are computed from
these records rather than from the tool.

## Tasks and grading

Five tasks per repository, one of each type: locate, modify, fix, explain, recall.
Answer keys were committed before the runs. Grading is automatic: deterministic
answer and edit graders for four types, and a model judge for the free-text explain
task, which the paper flags as requiring human confirmation.

## Licence

See LICENSE. Data under CC BY 4.0; the two included Python files under MIT.
