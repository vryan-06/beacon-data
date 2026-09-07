# gson, Sonnet tier, query (MCP) protocol

Second model tier (`claude-sonnet-5`, agent and judge), gson at the pinned corpus
SHA, `--runs 3`, `--after-protocol mcp`. Companion to `../gson-sonnet-read-runs3`
(the read protocol, which holds the shared `before` baseline).

**Shared baseline.** This run was launched with `--modes after` only. The `before`
(bare-repository) baseline is identical in expectation across protocols, so it was
measured once in `gson-sonnet-read-runs3` and reused here to save the expensive
Sonnet baseline spend. To compute the query-protocol delta, pair the `after` totals
in this directory against the `before` totals in `gson-sonnet-read-runs3/raw.json`.

**Headline (this tier).** Unlike the haiku tier (gson query protocol was about
-23%), on Sonnet the query protocol is roughly token-neutral (about +5% average
versus the shared baseline): Sonnet's bare-repo exploration is already lean, so the
query layer has little waste to remove. Correctness held (5/5 tasks pass, 0 wrong-file
edits). One of the fifteen `after` records grades `n/a`: run 1 of the explain
task, where the judge returned an unparseable verdict. Runs 0 and 2 of that task
both pass with detailed traces, so the task passes; the single record is excluded
rather than counted either way. See the paper's model-tier discussion for the full read/query/tier matrix.
