from alchemy import elements

def printer() -> None:
    print(f"Testing create_air: {elements.create_air()}")

def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    printer()

if __name__ == "__main__":
    main()