# fmt (C++), Sonnet tier, query (MCP) protocol

Second model tier (`claude-sonnet-5`, agent and judge), fmt at the pinned corpus
SHA (tag 11.0.2), `--runs 3`, `--modes before after --after-protocol mcp`. This run
carries its own `before` (bare-repository) baseline, so the query-protocol delta is
self-contained here.

**Headline (this tier).** On haiku the fmt query protocol was about -34%. On Sonnet
it is roughly token-neutral (about -1% average, +1.5% median): Sonnet explores the
bare repo efficiently, so the query layer has little exploration waste to remove.
Some localized tasks still win (modify -18.5%, locate -6.0%); the broad explain task
does not. Correctness held (5/5 pass, 0 wrong-file edits).

Together with `gson-sonnet-*`, this is the second language showing the same
model-tier dependence: the query-layer token win is large on a cheap model and
collapses to neutral on a strong one. See the paper's model-tier discussion.
