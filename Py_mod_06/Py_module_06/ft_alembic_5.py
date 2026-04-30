from alchemy import create_air

def printer() -> None:
    print(f"Testing create_air: {create_air()}")


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accesing the alchemy module using 'from alchemy import ...'")
    printer()

if __name__ == "__main__":
    main()
