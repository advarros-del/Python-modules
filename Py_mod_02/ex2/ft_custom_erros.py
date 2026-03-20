class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass
class WateringError(GardenError):
    pass

def custom_error_handler(plant_name: str) -> None:
    print("=== Custom Garden Errors ===")
    print("")
    print("Testing PlantError...")
    try:
        raise PlantError("Plant is wilting.")
    except PlantError:
        print(f"Caught PlantError: The {plant_name} plant is wilting.")
    print("Testing WateringError...")
    try:
        raise WateringError("Not getting enough water.")
    except WateringError:
        print(f"Caught WateringError: The {plant_name} plant is not getting enough water.")
    print("Testing caching all garden errors...")