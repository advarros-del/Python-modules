import alchemy.elements


def printer() -> None:
    print(f"Testing create_air: {alchemy.elements.create_earth()}")


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accesing Alchemy/elements.py using 'import ...' structure")
    printer()


if __name__ == "__main__":
    main()
