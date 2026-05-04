import alchemy

def printer() -> None:
    print(f"Testing create_air: {alchemy.create_air()}")

def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing Alchemy/elements.py using 'import ...' structure")
    printer()
    print("Now show that no all function can be reached")
    print("This will be raise an exception!")
#    try:
    print(f"{alchemy.create_earth()}")
##    except AttributeError as e:
#        print(f"Attribute Error: {e}")

if __name__ == "__main__":
    main()