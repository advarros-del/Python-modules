class PlantError(Exception):
    pass

def water_plant(plant_name) -> bool:
    try:
        if plant_name != str.capitalize(plant_name):
            raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    
        print(f"Watering {plant_name}: [OK]")
        return True

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending test and return to main")
        return False

def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("")
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        plants: list[str] = ["Tomato", "Lettuce", "Carrot"]
        plant: str
        for plant in plants:
            ok:bool = water_plant(plant)
            if not ok:  
                raise PlantError(f"Unexpected error watering plant: '{plant}'")
        print("Closing watering system")
        print("")

        print("Testing invalid plant...")
        print("Opening watering system")
        plants = ["Tomato", "lettuce", "Carrot"]
        for plant in plants:
            ok = water_plant(plant)
            if not ok:
                raise PlantError(f"Unexpected error watering plant: '{plant}'")
        
    except PlantError as e:
        print("Closing watering system")
    finally:
        print("")
        print("Cleanup always happens, even with errors!")

def main() -> None:
        test_watering_system()
        
if __name__ == "__main__":
    main()