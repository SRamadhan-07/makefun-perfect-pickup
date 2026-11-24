#!/usr/bin/env python3
"""Perfect pickup line — a make.fun entry.

The program writes one line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a pickup line an AI agent could say
aloud to a person, flattering and free to laugh off. The line is 75
characters, inside the competition's gate of 1 to 200 characters of
UTF-8 text. Standard library only, no network, and deterministic:
the same bytes on every run.
"""

import os

LINE = "Are you a CAPTCHA? Because I keep failing to prove I'm not falling for you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one line: no trailing newline, so
    # the text the judge reads is the line itself, byte for byte — the
    # gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
