# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| gson-locate-reflective-factory | 22761 | 21747 | -4% | pass → pass | 0 → 0 | 7 → 4 |
| gson-modify-gson-stub | 36159 | 41567 | +15% | pass → pass | 0 → 0 | 7 → 11 |
| gson-fix-enum-serializedname | 25906 | 34572 | +33% | pass → pass | 0 → 0 | 10 → 10 |
| gson-explain-deserialization-flow | 78690 | 78146 | -1% | pass → pass | 0 → 0 | 30 → 30 |
| gson-recall-jsonreaderinternalaccess | 19140 | 14955 | -22% | pass → pass | 0 → 0 | 9 → 4 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Avg tokens / task | 36531 | 38197 | +5% |
| Total wrong-file edits | 0 | 0 | — |
| Avg turns / task | 12.6 | 11.8 | — |
| Task success (pass) | 5/5 | 5/5 | maintained |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|
| gson-locate-reflective-factory | 22761 ± 20266 | 21747 ± 17367 |
| gson-modify-gson-stub | 36159 ± 5726 | 41567 ± 12486 |
| gson-fix-enum-serializedname | 25906 ± 5810 | 34572 ± 3547 |
| gson-explain-deserialization-flow | 78690 ± 14158 | 78146 ± 39403 |
| gson-recall-jsonreaderinternalaccess | 19140 ± 5085 | 14955 ± 1182 |

Paired Wilcoxon signed-rank (BEFORE vs AFTER token totals across 5 tasks): **p = 0.7874** _(under-powered: < 6 tasks — treat as directional)_

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
