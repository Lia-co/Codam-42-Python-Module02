#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


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
    test("100")
    test("-50")


if __name__ == "__main__":
    print("===  Garden Temperature Checker ===", end="\n\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
