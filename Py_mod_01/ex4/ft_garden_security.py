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

    def get_height(self) -> str:
        return (f"Heigth updated: {self.__height}cm")

    def get_age(self) -> str:
        return (f"Age updated: {self.__age} days")


def main() -> None:
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 25, 30)
    p1._Plant__height = 15
    p1._Plant__age = 10
    print(f"Plant created: {p1.name}: {p1._Plant__height}cm, {p1._Plant__age} days old\n")
    p1.set_height(25)
    p1.set_age(30)
    msg: str = p1.get_height()
    print(msg)
    msg = p1.get_age()
    print(msg)
    print("")
    p1.set_height(-6)
    p1.set_age(-12)
    print("")
    print(f"Current plant: {p1.name}: {p1._Plant__height}cm, {p1._Plant__age} days old")


if __name__ == "__main__":
    main()
