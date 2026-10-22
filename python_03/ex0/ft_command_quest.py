#!/usr/bin/env python3

import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {argc}")

if __name__ == "__main__":
    main()
