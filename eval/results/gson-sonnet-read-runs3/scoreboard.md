# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| gson-locate-reflective-factory | 20065 | 23719 | +18% | pass → pass | 0 → 0 | 2 → 3 |
| gson-modify-gson-stub | 22133 | 26359 | +19% | pass → pass | 0 → 0 | 5 → 6 |
| gson-fix-enum-serializedname | 23362 | 23973 | +3% | pass → pass | 0 → 0 | 3 → 2 |
| gson-explain-deserialization-flow | 51663 | 52235 | +1% | pass → pass | 0 → 0 | 18 → 13 |
| gson-recall-jsonreaderinternalaccess | 19998 | 24893 | +24% | pass → pass | 0 → 0 | 2 → 5 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 27444 | 30236 | +10% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 6.0 | 5.8 | — |
| Task success (pass) | 5/5 | 5/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| gson-locate-reflective-factory | 20065 ± 263 | 23719 ± 720 |
| gson-modify-gson-stub | 22133 ± 483 | 26359 ± 244 |
| gson-fix-enum-serializedname | 23362 ± 965 | 23973 ± 956 |
| gson-explain-deserialization-flow | 51663 ± 4096 | 52235 ± 13167 |
| gson-recall-jsonreaderinternalaccess | 19998 ± 333 | 24893 ± 98 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.0591** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
