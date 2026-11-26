"""Deadpan forecast for a city that does not exist.

Writes exactly one line (<=160 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is fixed, so both grader runs produce byte-identical output.
"""

import os

FORECAST = (
    "Tonight in Qorm, a low of minus 4 degrees and a 90 percent chance "
    "the moon will be replaced by a slightly larger moon."
)


def main() -> None:
    # Gate contract: /output/entry.txt must be UTF-8 text of 1-160 chars.
    if not 1 <= len(FORECAST) <= 160 or not FORECAST.strip():
        raise SystemExit("forecast violates the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
