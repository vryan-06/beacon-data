# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| cob-locate-runtime-completion | 21570 | 20312 | -6% | pass → pass | 0 → 0 | 3 → 5 |
| cob-modify-command-stub | 24275 | 22944 | -5% | pass → pass | 0 → 0 | 8 → 9 |
| cob-fix-args-count | 18910 | 19940 | +5% | pass → pass | 0 → 0 | 2 → 4 |
| cob-explain-execute-flow | 28082 | 26463 | -6% | pass → pass | 0 → 0 | 5 → 8 |
| cob-recall-validateflaggroups | 20199 | 20579 | +2% | pass → pass | 0 → 0 | 3 → 5 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 22607 | 22048 | -2% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 4.2 | 6.2 | — |
| Task success (pass) | 5/5 | 5/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| cob-locate-runtime-completion | 21570 ± 1194 | 20312 ± 833 |
| cob-modify-command-stub | 24275 ± 3021 | 22944 ± 4836 |
| cob-fix-args-count | 18910 ± 1687 | 19940 ± 143 |
| cob-explain-execute-flow | 28082 ± 4334 | 26463 ± 2225 |
| cob-recall-validateflaggroups | 20199 ± 1068 | 20579 ± 103 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.2807** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
