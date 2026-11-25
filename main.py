#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke, written to the grading output file."""

import os

# The joke: Monday doesn't knock — it files paperwork and starts the meeting.
# Second beat first, punchline last: the projector is the part nobody expects.
punchline = (
    "Monday showed up at 6 a.m. with a 47-slide presentation on everything "
    "I did wrong last week — and it brought its own projector."
)

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(punchline)

if __name__ == "__main__":
    main()
