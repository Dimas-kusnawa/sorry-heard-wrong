"""Sorry, I Heard That Wrong — make.fun entry.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt:
the apology a smart speaker gives after mishearing its owner.

Stdlib only, deterministic, no network, no clock, no randomness.
"""

import os

ENTRY = (
    "Sorry \u2014 I heard 'remind me to water the plants' as "
    "'remind me to water the pants,' so your jeans are soaking "
    "and the fern is furious."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
