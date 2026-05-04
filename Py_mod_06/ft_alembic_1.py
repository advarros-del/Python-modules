from elements import create_water

def printer() -> None:
    print(f"Testing create_water: {create_water()}")


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    printer()

if __name__ == "__main__":
    main()
