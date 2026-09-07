# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| cob-locate-runtime-completion | 31780 | 26591 | -16% | pass → pass | 0 → 0 | 11 → 8 |
| cob-modify-command-stub | 41478 | 38243 | -8% | pass → pass | 0 → 0 | 10 → 6 |
| cob-fix-args-count | 17634 | 12712 | -28% | pass → pass | 0 → 0 | 6 → 5 |
| cob-explain-execute-flow | 29459 | 18272 | -38% | pass → partial | 0 → 0 | 12 → 10 |
| cob-recall-validateflaggroups | 41753 | 22166 | -47% | pass → pass | 0 → 0 | 9 → 10 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 32421 | 23597 | -27% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 9.6 | 7.8 | — |
| Task success (pass) | 5/5 | 4/5 | regressed |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| cob-locate-runtime-completion | 31780 ± 20008 | 26591 ± 3360 |
| cob-modify-command-stub | 41478 ± 7819 | 38243 ± 2956 |
| cob-fix-args-count | 17634 ± 2655 | 12712 ± 546 |
| cob-explain-execute-flow | 29459 ± 20603 | 18272 ± 3963 |
| cob-recall-validateflaggroups | 41753 ± 27233 | 22166 ± 23317 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.0591** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
