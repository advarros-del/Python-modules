class Plant:
    num_plants: int = 0

    def __init__(self, name: str):
        self.name = name
        self.height = None
        self.age = None


    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Securoty: Negative height rejected")
        else:
            self.height = value
    
    
    def set_age(self, value: int)-> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Securoty: Negative age rejected")
        else:
            self.age = value


    def get_height(self) -> str:
        return (f"Heigth updated: {self.height}cm [OK]")


    def get_age(self) -> str:
        return (f"Age updated: {self.age} days [OK]")


def main ():
    print("=== Garden Security System ===")
    p1 = Plant("Rose")
    print(f"Plant created: {p1.name}")
    p1.set_height(25)
    p1.set_age(30)
    msg: str = p1.get_height()
    print(msg)
    msg = p1.get_age()
    print(msg)
    print("")
    p1.set_height(-6)
    print("")
    print(f"Current plant: {p1.name} ({p1.height}cm, {p1.age} days)")


if __name__ == "__main__":
    main()
