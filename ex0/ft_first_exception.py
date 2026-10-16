#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    def test(temp_str: str) -> None:
        try:
            print(f"Input data is '{temp_str}'")
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C", end="\n\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}", end="\n\n")

    test("25")
    test("abc")


if __name__ == "__main__":
    print("=== Garden Temperature ===", end="\n\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
