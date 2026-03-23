class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    pass


class WateringError(GardenError):
    pass


def custom_error_handler(plant_name: str) -> None:
    errors: list[GardenError] = []
    print("=== Custom Garden Errors ===")
    print("")
    print("Testing PlantError...")
    try:
        raise PlantError(
            f"Caught PlantError: The {plant_name} plant is wilting."
        )
    except PlantError as e:
        errors.append(e)
        print(
            f"Caught PlantError: The {plant_name} plant is wilting."
        )
    print("")
    print("Testing WateringError...")
    try:
        raise WateringError("Caught WateringError: "
                            "Not enough water in the tank!.")
    except WateringError as e:
        errors.append(e)
        print("Caught WateringError: "
              "Not enough water in the tank!.")
    print("")
    print("Testing caching all garden errors...")
    for error in errors:
        print(f" - {error}")
    print("")
    print("All custom erros tyeps work correctly.")


custom_error_handler("Tomato")
