import alchemy 

def printer() -> None:
    print(f"Testing create_earth: {create_earth()}")

def main() -> None:
    print("=== Alembic 4 ===")
    print("Using: 'import ...' structure to access elements.py")
    printer()

if __name__ == "__main__":
    main()
