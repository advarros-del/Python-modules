import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archive Recovery ===")
    print(f"Accesing file '{sys.argv[1]}'")
    try:
        f: typing.IO = open(sys.argv[1], "r")
        print("---\n")
        print(f.read())
        f.close()
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
