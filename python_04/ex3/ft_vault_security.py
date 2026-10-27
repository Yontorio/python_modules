#!/usr/bin/env python3


def secure_archive(filename: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if mode not in ("r", "w"):
        return (False, f"Unsupported action: {mode}")
    try:
        with open(filename, mode) as file:
            if mode == "r":
                data: str = file.read()
                return (True, data)
            file.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    result: tuple[bool, str]

    result = secure_archive("/not/existing/file")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(result)

    result = secure_archive("/etc/master.passwd")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(result)

    result = secure_archive("ancient_fragment.txt")
    print("Using 'secure_archive' to read from a regular file:")
    print(result)

    result = secure_archive("vault_copy.txt", "w", result[1])
    print("Using 'secure_archive' to write previous content"
          " to a new file:")
    print(result)


if __name__ == "__main__":
    main()
