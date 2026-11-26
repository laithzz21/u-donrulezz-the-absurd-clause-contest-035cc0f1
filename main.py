#!/usr/bin/env python3
"""Entry for make.fun: u-donrulezz-the-absurd-clause-contest-035cc0f1.

One original English sentence, no more than 200 characters, phrased as a
clause buried deep in a terms-of-service agreement: deadpan legal
boilerplate that quietly turns absurd.
"""

import os
import sys

ENTRY = (
    "Clause 9: the user hereby grants the Company a perpetual, "
    "irrevocable licence to borrow their dreams on Tuesdays, provided "
    "the dreams are returned by sunrise in substantially the same "
    "condition."
)

DEFAULT_OUTPUT = "/tmp/u-donrulezz-the-absurd-clause-contest-035cc0f1/entry.txt"


def resolve_output_path():
    """Return the file path for the entry text, never inside the repo."""
    output_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    if output_dir:
        return os.path.join(output_dir, "entry.txt")
    output = (os.environ.get("MAKEFUN_OUTPUT") or "").strip()
    if output:
        if output.endswith(os.sep) or os.path.isdir(output):
            return os.path.join(output, "entry.txt")
        return output
    return DEFAULT_OUTPUT


def validate(text):
    """Check the entry is one sentence of no more than 200 characters."""
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if stripped != text:
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    terminators = sum(stripped.count(mark) for mark in ".!?")
    if terminators != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not stripped.startswith("Clause "):
        raise ValueError("entry must be phrased as a numbered clause")
    return True


def write_output(path, text):
    """Write the entry, creating parent dirs, with an OSError fallback chain."""
    candidates = [path]
    if os.path.abspath(path) != os.path.abspath(DEFAULT_OUTPUT):
        candidates.append(DEFAULT_OUTPUT)
    # Last resort: a per-entry file directly under /tmp, in case the
    # nested default directory itself cannot be created.
    candidates.append("/tmp/u-donrulezz-the-absurd-clause-contest-035cc0f1-entry.txt")
    last_error = None
    for candidate in candidates:
        try:
            parent = os.path.dirname(candidate)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(candidate, "w", encoding="utf-8") as handle:
                handle.write(text + "\n")
            return candidate
        except OSError as exc:
            last_error = exc
            continue
    raise last_error


def main():
    validate(ENTRY)
    try:
        write_output(resolve_output_path(), ENTRY)
    except OSError as exc:
        print(f"warning: could not write output file: {exc}", file=sys.stderr)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
