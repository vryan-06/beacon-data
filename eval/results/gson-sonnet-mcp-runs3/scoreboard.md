# Eval scoreboard

| Task | Tokens BEFORE | Tokens AFTER | Token Δ | Success (B → A) | Wrong edits (B → A) | Turns (B → A) |
|---|--:|--:|--:|:--:|:--:|:--:|
| gson-locate-reflective-factory | — | 20001 | — | — → pass | 0 → 0 | — → 3 |
| gson-modify-gson-stub | — | 22200 | — | — → pass | 0 → 0 | — → 5 |
| gson-fix-enum-serializedname | — | 22668 | — | — → pass | 0 → 0 | — → 4 |
| gson-explain-deserialization-flow | — | 57834 | — | — → pass | 0 → 0 | — → 22 |
| gson-recall-jsonreaderinternalaccess | — | 20810 | — | — → pass | 0 → 0 | — → 4 |

## Headline

| Metric | BEFORE | AFTER | Improvement |
|---|--:|--:|:--:|
| Total wrong-file edits | 0 | 0 | — |
| Task success (pass) | 0/0 | 5/5 | — |

## Statistics (up to 3 runs per task/mode)

| Task | Tokens BEFORE (mean ± 95% CI) | Tokens AFTER (mean ± 95% CI) |
|---|--:|--:|

_Significance test needs ≥ 2 tasks with paired runs (have 0) — it activates once the repo corpus (WI-5) is in._

_Task success is computed automatically (WI-1): the `file` grader passes a run iff the agent reached every pre-declared answer-key file and — for edit tasks — edited nothing outside it; the optional `judge` grader scores free-text answers via an LLM and must be human-validated before it is trusted._
_5 task(s) had a BEFORE and/or AFTER run error (see the ERROR cells above and raw.json for details) — excluded from the headline averages rather than counted as 0 tokens._
