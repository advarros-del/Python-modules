class Plant:
    num_plants: int = 0

    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.__height: int = height
        self.__age: int = age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative!")
            print("Height  uptadte rejected")
        else:
            self.__height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative!")
            print("Age  uptadte rejected")
        else:
            self.__age = value

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


def main() -> None:
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15, 10)
    print(
        f"Plant created: {p1.name}: {p1.get_height()}cm, "
        f" {p1.get_age()} days old\n"
    )
    p1.set_height(25)
    print(f"Height updated: {p1.get_height()}")
    p1.set_age(30)
    print(f"Age updated: {p1.get_age()}\n")
    p1.set_height(-6)
    p1.set_age(-12)
    print("")
    print(
        f"Current plant: {p1.name}: {p1.get_height()}cm, "
        f"{p1.get_age()} days old"
    )


if __name__ == "__main__":
    main()
