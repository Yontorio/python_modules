#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()

    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()

    try:
        print(f"Temperature is now {input_temperature('100')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()

    try:
        print(f"Temperature is now {input_temperature('-50')}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
