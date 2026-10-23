#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
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

    transformed: str = content.replace("\n", "#\n")
    if content and not content.endswith("\n"):
        transformed += "#"

    print("\nTransform data:")
    print(f"---\n\n{transformed}\n---")

    new_filename: str = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out: IO[str]
    try:
        out = open(new_filename, "w")
    except OSError as e:
        print(f"Error opening file '{new_filename}': {e}")
        print("Data not saved.")
        return

    try:
        out.write(transformed)
    except OSError as error:
        print(f"Error writing to file '{new_filename}': {error}")
        print("Data not saved.")
        return
    finally:
        out.close()
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
