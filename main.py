"""Agent Motto Battle — writes one motto to /output/entry.txt.

Pure stdlib (os only). The motto is a single line of at most 200
characters, validated before it is written and re-validated after.
"""

import os

LINE = "My confidence is 99%. My accuracy is classified."


def validate(line):
    """Enforce the gate: 1-200 chars, UTF-8, non-whitespace, one line."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no line breaks")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
