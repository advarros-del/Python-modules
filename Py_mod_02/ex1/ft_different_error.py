def garden_operation() -> None:
    try:
        value = int("abc")
    except ValueError:
        print("Error: Invalid value")
    try:
        result: int = 10/0
    except ZeroDivisionError:
        print("Error: Division by zero")
    try:
        open("failed_file.txt", "r")
    except FileNotFoundError:
        print("Error: File not found")
    try:
        plant = {"Rose", 26}
        garden = plant["sunflower"]
    except KeyError:
        print("Error: Plant not found")


def test_errors_types(thing) -> None:
    print("=== Garden Error Types ===")
    garden_operation()
    print("All error types tested successfully!")


def main() -> None:
    test_errors_types(None)


if __name__ == "__main__":
    main()