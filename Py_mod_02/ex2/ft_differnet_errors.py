def garden_operation(operation_number: int) -> None:
    if operation_number == 0:
        result: int = int("abc")
        print(result)
    elif operation_number == 1:
        n: float = 10 / 0
        print(n)
    elif operation_number == 2:
        open("non_existent_file.txt", "r")
    elif operation_number == 3:
        result = "Hello, " + 5
        print(result)
    else:
        return


def test_errors_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operation(i)
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("Operation complete successfully.\n")
    print("All error types tested successfully.")


def main() -> None:
    test_errors_types()


if __name__ == "__main__":
    main()
