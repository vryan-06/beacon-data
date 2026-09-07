# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| req-locate-redirects | 24540 | 17526 | -29% | pass → pass | 0 → 0 | 7 → 11 |
| req-modify-preparedrequest | 27420 | 16579 | -40% | pass → pass | 0 → 0 | 5 → 7 |
| req-fix-encoding | 22493 | 27085 | +20% | pass → pass | 0 → 0 | 10 → 19 |
| req-explain-lifecycle | 39404 | 44777 | +14% | partial → partial | 0 → 0 | 12 → 22 |
| req-recall-extract-cookies | 25631 | 10867 | -58% | pass → pass | 0 → 0 | 16 → 4 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 27898 | 23367 | -16% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 10.0 | 12.6 | — |
| Task success (pass) | 4/5 | 4/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| req-locate-redirects | 24540 ± 14190 | 17526 ± 6641 |
| req-modify-preparedrequest | 27420 ± 1471 | 16579 ± 3481 |
| req-fix-encoding | 22493 ± 10872 | 27085 ± 17645 |
| req-explain-lifecycle | 39404 ± 75491 | 44777 ± 2040 |
| req-recall-extract-cookies | 25631 ± 4016 | 10867 ± 676 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.2807** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
