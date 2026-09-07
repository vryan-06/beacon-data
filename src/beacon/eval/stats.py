"""WI-2: dependency-free statistics for the multi-run eval.

Two things the scoreboard needs once a task is run more than once:
  - ``mean_ci`` — a mean with a 95% confidence-interval half-width (Student-t based),
    so token/turn numbers report as ``mean ± h`` instead of a single lucky sample.
  - ``wilcoxon_signed_rank`` — a paired, non-parametric significance test for
    BEFORE-vs-AFTER token totals across tasks (agent loops aren't normally
    distributed, so a paired t-test would be the wrong tool).

No numpy/scipy — the corpus is tiny and pinning heavyweight deps for two formulas
isn't worth it. The Wilcoxon p-value uses the standard normal approximation with a
continuity correction and tie correction; for very small n (< ~6 pairs) it is
under-powered and the caller should say so rather than over-claim significance.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# Two-sided 95% Student-t critical values by degrees of freedom (df = n-1).
# df > 30 falls back to the normal 1.96 — the difference is < 2% there.
_T95 = {
    1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365,
    8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145,
    15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080,
    22: 2.074, 23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048,
    29: 2.045, 30: 2.042,
}


def _t_crit_95(df: int) -> float:
    if df <= 0:
        return 0.0
    return _T95.get(df, 1.96)


@dataclass(frozen=True)
class MeanCI:
    mean: float
    half_width: float  # 95% CI half-width; 0.0 when n < 2 (no spread estimate)
    n: int

    def __str__(self) -> str:
        if self.n < 2:
            return f"{self.mean:.0f}"
        # A small-but-nonzero CI must not render as "± 0" — keep 2 sig figs under 0.5.
        hw = f"{self.half_width:.0f}" if self.half_width >= 0.5 else f"{self.half_width:.2g}"
        return f"{self.mean:.0f} ± {hw}"


def mean_ci(values: list[float], confidence: float = 0.95) -> MeanCI:
    """Sample mean with a Student-t 95% CI half-width. n<2 → half_width 0.0."""
    n = len(values)
    if n == 0:
        return MeanCI(mean=0.0, half_width=0.0, n=0)
    mean = sum(values) / n
    if n < 2:
        return MeanCI(mean=mean, half_width=0.0, n=n)
    var = sum((v - mean) ** 2 for v in values) / (n - 1)  # sample variance
    se = math.sqrt(var) / math.sqrt(n)
    return MeanCI(mean=mean, half_width=_t_crit_95(n - 1) * se, n=n)


def _norm_sf(z: float) -> float:
    """Upper-tail standard-normal survival function P(Z > z), via erf."""
    return 0.5 * math.erfc(z / math.sqrt(2.0))


@dataclass(frozen=True)
class WilcoxonResult:
    statistic: float  # W = min(W+, W-)
    p_value: float    # two-sided
    n: int            # non-zero-difference pairs used
    underpowered: bool  # n < 6 → normal approximation is unreliable


def wilcoxon_signed_rank(before: list[float], after: list[float]) -> WilcoxonResult:
    """Paired Wilcoxon signed-rank test (two-sided) on ``after - before`` differences.

    Zero differences are dropped (standard). p-value uses the normal approximation
    with continuity + tie correction. Empty/all-zero input → p = 1.0.
    """
    if len(before) != len(after):
        raise ValueError("before/after must be the same length (paired)")
    diffs = [a - b for b, a in zip(before, after) if (a - b) != 0]
    n = len(diffs)
    if n == 0:
        return WilcoxonResult(statistic=0.0, p_value=1.0, n=0, underpowered=True)

    # Average-rank the absolute differences (ties share the mean of their ranks).
    order = sorted(range(n), key=lambda i: abs(diffs[i]))
    ranks = [0.0] * n
    i = 0
    tie_sizes: list[int] = []
    while i < n:
        j = i
        while j + 1 < n and abs(diffs[order[j + 1]]) == abs(diffs[order[i]]):
            j += 1
        avg_rank = (i + 1 + j + 1) / 2.0  # ranks are 1-based
        for k in range(i, j + 1):
            ranks[order[k]] = avg_rank
        tie_sizes.append(j - i + 1)
        i = j + 1

    w_plus = sum(r for d, r in zip(diffs, ranks) if d > 0)
    w_minus = sum(r for d, r in zip(diffs, ranks) if d < 0)
    w = min(w_plus, w_minus)

    mean_w = n * (n + 1) / 4.0
    tie_term = sum(t ** 3 - t for t in tie_sizes)
    var_w = (n * (n + 1) * (2 * n + 1) - tie_term / 2.0) / 24.0
    if var_w <= 0:
        return WilcoxonResult(statistic=w, p_value=1.0, n=n, underpowered=n < 6)
    z = (abs(w - mean_w) - 0.5) / math.sqrt(var_w)  # continuity correction
    p = min(1.0, 2.0 * _norm_sf(z))
    return WilcoxonResult(statistic=w, p_value=p, n=n, underpowered=n < 6)
