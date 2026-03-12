class Plant:
    num_plants: int = 0

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        Plant.num_plants += 1


def printer_function(plant_variety) -> None:
    for i in plant_variety:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")


def main():
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Oak", 200, 365)
    p5 = Plant("Fern", 15, 120)
    plant_variety = [p1, p2, p3, p4, p5]
    printer_function(plant_variety)
    print("")
    print(f"Total plants created: {Plant.num_plants}")


if __name__ == "__main__":
    main()
