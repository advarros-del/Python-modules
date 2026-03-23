class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show() -> None:
        p1 = Plant(
            name="Rose",
            height=25,
            age=30,
        )
        p2 = Plant(
            name="Sunflower",
            height=80,
            age=45,
        )
        p3 = Plant(
            name="Cactus",
            height=15,
            age=120,
        )
        plants = [p1, p2, p3]
        for i in range(3):
            p = plants[i]
            print(f"{p.name}: {p.height}cm, {p.age} days old.")


def main():
    print("=== Garden Plant Registry ===")
    Plant.show()


if __name__ == "__main__":
    main()
