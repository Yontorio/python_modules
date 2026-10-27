#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()

    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
