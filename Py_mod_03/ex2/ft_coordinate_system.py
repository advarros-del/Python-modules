import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        aux: str = (input("Enter new coordinates as floats format 'x,y,z': "))
        if aux.count(',') != 2:
            raise SyntaxError("Invalid syntax")
    except SyntaxError as e:
        print(e)
        return get_player_pos()
    a: str
    b: str
    c: str
    a, b, c = aux.split(',')
    try:
        x: float = float(a)
    except ValueError:
        print(f"Error on parameter '{a}': "
              f"could not convert string to float: {a}")
        return get_player_pos()
    try:
        y = float(b)
    except ValueError:
        print(f"Error on parameter '{b}': "
              f"could not convert string to float: {b}")
        return get_player_pos()
    try:
        z = float(c)
    except ValueError:
        print(f"Error on parameter '{c}': "
              f"could not convert string to float: {c}")
        return get_player_pos()
    Coor: tuple[float, float, float] = (x, y, z)
    return Coor


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    Coor1: tuple[float, float, float] = get_player_pos()
    print(f" Got the first tuple: ({Coor1[0]}, {Coor1[1]}, {Coor1[2]})")
    print(f"It includes: X={Coor1[0]}, Y={Coor1[1]}, Z={Coor1[2]}")
    distance1: float = math.sqrt((0 - Coor1[0])**2 +
                                 (0 - Coor1[1])**2 + (0 - Coor1[2])**2)
    print(f"Distance to center: {distance1:.4f}\n")
    print("Get a second set of coordinates")
    Coor2: tuple[float, float, float] = get_player_pos()
    distance2: float = math.sqrt((Coor2[0] - Coor1[0])**2 +
                                 (Coor2[1] - Coor1[1])**2 +
                                 (Coor2[2] - Coor1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance2:.4f}")


if __name__ == "__main__":
    main()
