"""Before/after evaluation: measure an AI agent's token spend on a repo with and
without Beacon's generated .ai/ knowledge layer.

Primitives shared by the ``beacon demo`` command (see ``demo.py``) and the standalone
research harness (``eval/run_eval.py`` at the repo root, which re-exports from here):

  types       Task / TaskResult dataclasses (the A/B measurement unit).
  isolation   Throwaway working copies — git worktree (for the root harness) and a
              git-free folder-copy + content-hash diff (for ``beacon demo``, so it works
              on any folder, tracked or not).
  runner      Drives a real ``claude -p`` tool-use loop and records its usage.
  scoreboard  Renders the BEFORE/AFTER markdown table + raw json.
  taskgen     Auto-generates grounded eval tasks from repo-map.json.
  demo        Orchestrates the full ``beacon demo`` flow.
"""
