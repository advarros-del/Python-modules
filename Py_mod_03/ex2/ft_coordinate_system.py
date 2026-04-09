import math

def get_player_pos() -> None:
    try:
        aux: str = (input("Enter new coordinates as floats format 'x,y,z': "))
        if aux.count(',') != 2:
            raise SyntaxError("Invalid syntax")
    except SyntaxError as e:
        print(e)
        return get_player_pos()
    x, y, z = aux.split(',')
    try:
        x: float = float(x)
    except ValueError as e:
        print(f"Error on parameter '{x}': could not convert string to float: {x}")
        return get_player_pos()
    try:
        y: float = float(y)
    except ValueError as e:
        print(f"Error on parameter '{y}': could not convert string to float: {y} ")
        return get_player_pos()
    try:
        z: float = float(z)
    except ValueError as e:
        print(f"Error on parameter '{z}': could not convert string to float: {z}")
        return get_player_pos()
    Coor: tuple[float, float, float] = (x, y, z)
    return Coor

def main() -> None:
    print("=== Game Coordinate System ===\n")
    Coor1: tuple[float, float, float] = get_player_pos()
    print(f" Got the first tuple: ({Coor1[0]}, {Coor1[1]}, {Coor1[2]})")
    print(f"It includes: X={Coor1[0]}, Y={Coor1[1]}, Z={Coor1[2]}")
    distance1: float = math.sqrt((0 - Coor1[0])**2 + (0 - Coor1[1])**2 + (0 - Coor1[2])**2)
    print(f"Distance to center: {distance1:.4f}\n")
    Coor2: tuple[float, float, float] = get_player_pos()
    distance2: float = math.sqrt((Coor2[0] - Coor1[0])**2 + (Coor2[1] - Coor1[1])**2 + (Coor2[2] - Coor1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance2:.4f}")

    
if __name__ == "__main__":
        main()
