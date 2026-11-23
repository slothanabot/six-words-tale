"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).
Deterministic, no network, no model calls, no file reads.
"""

import os


STORY = "His last light outlived him, burning."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
