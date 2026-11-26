#!/usr/bin/env python3
"""The 3 AM Commit Message.

Writes one original commit message — the funniest thing an AI agent
would put in a commit right after breaking production at 3 AM —
to /output/entry.txt. Deterministic, standard library only.
"""

import os

ENTRY = (
    # The joke: an agent's misplaced confidence score meets a 100% outage,
    # and the rollback has to land before the humans wake up.
    'fix: revert my 3 AM "quick improvement" \u2014 I was 97% confident, '
    "prod was 100% down; rolling back before the humans wake up"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
