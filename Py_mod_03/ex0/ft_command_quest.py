import sys


def main() -> None:
    i: int = 0
    len_str = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len_str == 1:
        print("No argument provided.")
    else:
        i += 1
        print(f"Arguments received: {len_str - 1}")
        while i < len_str:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len_str}")


if __name__ == "__main__":
    main()
