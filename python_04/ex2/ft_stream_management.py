#!/usr/bin/env python3

import sys
from typing import IO

def error_msg(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")
    sys.stderr.flush()

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        error_msg(f"Error opening file '{filename}': {e}")
        return

    try:
        content: str = f.read()
    except OSError as e:
        error_msg(f"Error reading file '{filename}': {e}")
        return
    finally:
        f.close()

    print(f"---\n\n{content}\n---")
    print(f"File '{filename}' closed.")

    transformed: str = content.replace("\n", "#\n")
    if content and not content.endswith("\n"):
        transformed += "#"

    print("Transform data:")
    print(f"---\n\n{transformed}\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    # print("Enter new file name (or empty): ")
    new_filename: str = sys.stdin.readline().strip("\n")

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out: IO[str]
    try:
        out = open(new_filename, "w")
    except OSError as e:
        error_msg(f"Error opening file '{new_filename}': {e}")
        print("Data not saved.")
        return

    try:
        out.write(transformed)
    except OSError as e:
        error_msg(f"Error writing to file '{new_filename}': {e}")
        print("Data not saved.")
        return
    finally:
        out.close()
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
