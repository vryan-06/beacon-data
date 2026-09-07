# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| fmt-locate-dragonbox-to-decimal | 21648 | 20347 | -6% | pass → pass | 0 → 0 | 5 → 3 |
| fmt-modify-memory-buffer-is-empty | 36421 | 29695 | -18% | pass → pass | 0 → 0 | 15 → 8 |
| fmt-fix-file-size-largefile | 20970 | 23015 | +10% | pass → pass | 0 → 0 | 3 → 4 |
| fmt-explain-format-to-output-flow | 56049 | 59724 | +7% | pass → pass | 0 → 0 | 22 → 32 |
| fmt-recall-format-error-code-uses | 24298 | 24665 | +2% | pass → pass | 0 → 0 | 5 → 8 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 31877 | 31489 | -1% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 10.0 | 11.0 | — |
| Task success (pass) | 5/5 | 5/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| fmt-locate-dragonbox-to-decimal | 21648 ± 1353 | 20347 ± 42 |
| fmt-modify-memory-buffer-is-empty | 36421 ± 40211 | 29695 ± 11146 |
| fmt-fix-file-size-largefile | 20970 ± 918 | 23015 ± 491 |
| fmt-explain-format-to-output-flow | 56049 ± 21766 | 59724 ± 29275 |
| fmt-recall-format-error-code-uses | 24298 ± 11232 | 24665 ± 3391 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 1.0000** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
