# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| me-locate-flags | 20324 | 19137 | -6% | pass → pass | 0 → 0 | 6 → 5 |
| me-modify-containers | 37886 | 24251 | -36% | pass → pass | 0 → 0 | 6 → 7 |
| me-fix-range | 21788 | 25508 | +17% | pass → pass | 0 → 0 | 9 → 7 |
| me-explain-enum-name | 68579 | 60487 | -12% | partial → pass | 0 → 0 | 25 → 30 |
| me-recall-flags-tests | 31283 | 36252 | +16% | pass → pass | 0 → 0 | 26 → 16 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 35972 | 33127 | -8% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 14.4 | 13.0 | — |
| Task success (pass) | 4/5 | 5/5 | improved |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| me-locate-flags | 20324 ± 13890 | 19137 ± 15851 |
| me-modify-containers | 37886 ± 3832 | 24251 ± 18959 |
| me-fix-range | 21788 ± 16902 | 25508 ± 20507 |
| me-explain-enum-name | 68579 ± 18118 | 60487 ± 38396 |
| me-recall-flags-tests | 31283 ± 14355 | 36252 ± 56603 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.5896** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
