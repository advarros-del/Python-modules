import alchemy.elements

def printer() -> None:
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")

def main() -> None:
    print("=== Alembic 2 ===")
    print("Using: 'import ...' structure to access elements.py")
    printer()

if __name__ == "__main__":
    main()
