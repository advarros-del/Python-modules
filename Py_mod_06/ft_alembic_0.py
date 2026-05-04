import elements

def printer() -> None:
    print(f"Testing create_fire: {elements.create_fire()}")

def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    printer()
    
if __name__ == "__main__":
    main()
