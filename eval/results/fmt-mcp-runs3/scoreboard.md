# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| fmt-locate-dragonbox-to-decimal | 23446 | 12662 | -46% | pass → pass | 0 → 0 | 8 → 4 |
| fmt-modify-memory-buffer-is-empty | 22481 | 15702 | -30% | pass → pass | 0 → 0 | 10 → 8 |
| fmt-fix-file-size-largefile | 21184 | 14841 | -30% | pass → pass | 0 → 0 | 6 → 4 |
| fmt-explain-format-to-output-flow | 86634 | 65006 | -25% | partial → partial | 0 → 0 | 49 → 43 |
| fmt-recall-format-error-code-uses | 22884 | 13464 | -41% | pass → pass | 0 → 0 | 11 → 7 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 35326 | 24335 | -31% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 16.8 | 13.2 | — |
| Task success (pass) | 4/5 | 4/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| fmt-locate-dragonbox-to-decimal | 23446 ± 10264 | 12662 ± 1955 |
| fmt-modify-memory-buffer-is-empty | 22481 ± 7635 | 15702 ± 1686 |
| fmt-fix-file-size-largefile | 21184 ± 7086 | 14841 ± 2620 |
| fmt-explain-format-to-output-flow | 86634 ± 25436 | 65006 ± 30842 |
| fmt-recall-format-error-code-uses | 22884 ± 5390 | 13464 ± 4723 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.0591** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
