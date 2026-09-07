# cobra (Go), Sonnet tier, query (MCP) protocol

Second model tier (`claude-sonnet-5`, agent and judge), cobra at the pinned corpus
SHA, `--runs 3`, `--modes before after --after-protocol mcp`. Carries its own
`before` (bare-repository) baseline.

**Headline (this tier).** On haiku the cobra query protocol was about -27%. On
Sonnet it is about -2% average (near-neutral). Fourth language (Go) confirming the
model-tier collapse seen on gson (Java), fmt (C++) and requests (Python): the
query-layer token win is large on a cheap model and shrinks toward neutral on a
strong one. Per-task the Sonnet deltas are all small (locate/modify/explain about
-6%, fix +5%, recall +2%). Correctness held (5/5 pass, 0 wrong-file edits).

Completes the 4-language x 2-tier matrix. Pooled query-protocol delta: about -27%
at the haiku tier, about -1% at the Sonnet tier. See the paper's model-tier
discussion.
