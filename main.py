#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes one original line (the funniest last words a phone says as its
battery hits 1 percent) to /output/entry.txt, and prints the same line
to stdout. Stdlib only, deterministic: the same bytes on every run.

The joke: the phone speaks in its own system-notification voice
("Low battery: 1% remaining") and then reframes its death as quitting
its job — the warning is a resignation letter. No will reading, no
goodbye to the charger, no pun on 1 percent, no autocorrect gag, no
dying mid-word: the twist is the phone as an overworked employee
handing in its notice at the exact moment it runs out of power.
"""

import os

ENTRY = (
    "Low battery: 1% remaining. "
    "This isn't a warning \u2014 it's my resignation letter."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
