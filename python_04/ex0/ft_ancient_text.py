#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        content: str = f.read()
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
        return
    finally:
        f.close()

    print(f"---\n\n{content}\n---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
