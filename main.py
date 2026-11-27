"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (151 code points) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
Deterministic: the same bytes on every run. Standard library only,
no network, no dependencies outside this repository.

The output is written with no trailing newline and no BOM, so the file
holds exactly the 151 characters the gate counts (1-240 allowed).
"""

import os

TEXT = (
    "The girl who stuttered read the morning announcements to the whole "
    "school, and when she finished she folded the paper in four and put "
    "it in her pocket."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
