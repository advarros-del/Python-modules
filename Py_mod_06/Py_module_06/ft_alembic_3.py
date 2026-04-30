from alchemy.elements import create_air

def printer() -> None:
    print(f"Testing create_earth: {create_air()}")
    
from alchemy.elements import create_air

def printer() -> None:
    print(f"Testing create_air: {create_air()}")
    
def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using : 'from ... import ...' structure")
    printer()

if __name__ == "__main__":
    main()
