class Plant:
    num_plants: int = 0

    def __init__(self, name: str):
        self.name = name
        self.height = None
        self.age = None


def set_height(self, value: int) -> None:
     if value < 0:
        print("Invalid operation attempted: height {value}cm [REJECTED]")
        print("Securoty: Negative height rejected")
     else:
        self.heigth = value
    
    
def set_age(self, value: int)-> None:
    if value < 0:
        print("Invalid operation attempted: age {value} days [REJECTED]")
        print("Securoty: Negative age rejected")
    else:
        self.age = value


def get_height(self) -> str:
    return (f"Heigth updated: {p1.heigth}cm [OK]")


def get_age(self) -> str:
    return (f"Age updated: {p1.age} days [OK]")


def main ():
    print("=== Garden Security System ===")
    p1 = Plant("Rose")
    p1.set_heigth(25)
    p1.set_age(30)
    p1.get_heigth()
    p1.get_age()
    print("")
    set_heigth(-6)
    print("")
    print(f"Current plant: {p1.name} ({p1.heigth}cm, {p1.age} days")


if __name__ == "__main__":
    main()
