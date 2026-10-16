#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_name_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for _ in plant_name_list:
            water_plant(_)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===", end="\n\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()
    print("Cleanup always happens, even with errors!")
