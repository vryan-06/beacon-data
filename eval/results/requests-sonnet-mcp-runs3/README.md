# requests (Python), Sonnet tier, query (MCP) protocol

Second model tier (`claude-sonnet-5`, agent and judge), requests at the pinned
corpus SHA, `--runs 3`, `--modes before after --after-protocol mcp`. Carries its
own `before` (bare-repository) baseline.

**Headline (this tier).** On haiku the requests query protocol was about -18%. On
Sonnet it is about -5% average (near-neutral). Same model-tier collapse seen on
gson (Java) and fmt (C++): the query-layer token win is large on a cheap model and
shrinks toward neutral on a strong one. Per-task the picture is noisier here
(explain -20.9%, recall +4.9%), but the aggregate direction matches. Correctness
held (5/5 pass, 0 wrong-file edits).

Third language confirming the model-tier dependence. See the paper's model-tier
discussion for the full read/query/tier matrix.
