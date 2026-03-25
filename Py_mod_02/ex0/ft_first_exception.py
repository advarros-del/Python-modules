def test_temperature() -> None:
    print("=== Garden Temperatue ===")
    input_temperature("25")
    input_temperature("abc")
    print("All test completed - program didn't crash!")


def input_temperature(temp_str: str) -> int:
    print("")
    print(f"Input data: '{temp_str}'")
    try:
        int(temp_str)
    except ValueError:
        print(
            f"Caught inpu_temperature error: invalid"
            f"literal for int() with base 10: '{temp_str}'"
            )
        return 1
    print(f"Temperature is now {temp_str}")
    return int(temp_str)


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
