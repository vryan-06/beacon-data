# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| req-locate-redirects | 20299 | 19581 | -4% | pass → pass | 0 → 0 | 2 → 3 |
| req-modify-preparedrequest | 25062 | 23963 | -4% | pass → pass | 0 → 0 | 6 → 6 |
| req-fix-encoding | 20577 | 20236 | -2% | pass → pass | 0 → 0 | 3 → 4 |
| req-explain-lifecycle | 46676 | 36929 | -21% | pass → pass | 0 → 0 | 8 → 15 |
| req-recall-extract-cookies | 21172 | 22212 | +5% | pass → pass | 0 → 0 | 3 → 8 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 26757 | 24584 | -8% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 4.4 | 7.2 | — |
| Task success (pass) | 5/5 | 5/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| req-locate-redirects | 20299 ± 1074 | 19581 ± 428 |
| req-modify-preparedrequest | 25062 ± 6288 | 23963 ± 5282 |
| req-fix-encoding | 20577 ± 319 | 20236 ± 3068 |
| req-explain-lifecycle | 46676 ± 4732 | 36929 ± 2232 |
| req-recall-extract-cookies | 21172 ± 1222 | 22212 ± 579 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.2807** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
