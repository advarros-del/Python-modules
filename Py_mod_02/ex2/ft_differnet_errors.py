def garden_operation(operation_number) -> None:
    if operation_number == 0:
        result: int = int("abc")
    elif operation_number == 1:
        result: int = 10 / 0
    elif operation_number == 2:
        open("non_existent_file.txt", "r")
    elif operation_number == 3:
        flower: dict[str, str | int] = {"name": "Rose", "color": "red", "count": 45}
        comunity = flower["blue"]
    else:
        return


def test_errors_types() -> None:
    
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operation(i)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except ValueError:
            print("Caught ValueError: invalid literal for int() with base 10: 'abc'")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'")
        except KeyError:
            print("Caught KeyError: can only concatenate str (not 'int') to str")
    print("Operation complete successfully.")
    print("")
    print("All error types tested successfully.")


test_errors_types()
