from alchemy.elements import create_earth, create_air

def printer() -> None:
    print(f"Testing create_earth: {create_earth()}")

def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing Alchemy/elements.py using 'from ... import ...' structure")
    printer()

if __name__ == "__main__":
    main()
