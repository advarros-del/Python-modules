class Plant:
    num_plants: int = 0

    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


def printer_function(plant_variety: list[Plant]) -> None:
    for i in plant_variety:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")


def main() -> None:
    print("=== Plant Factory Output ===")
    plant_variety: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 5, 90),
        Plant("Oak", 200, 365),
        Plant("Fern", 15, 120),
    ]
    printer_function(plant_variety)


if __name__ == "__main__":
    main()
