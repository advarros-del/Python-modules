import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archive Recovery & Preservation ===")
    print(f"Accesing file '{sys.argv[1]}'")
    try:
        f: typing.IO = open(sys.argv[1], "r")
        print("---\n")
        try:
            copy: typing.IO = f.read()
            print(copy)
        finally:
            f.close()
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.")
        
    except (OSError, ValueError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
    print("\nTransform data:\n---\n")
    final_text: str = ""
    for i in range(len(copy)):
        if copy[i] == "\n" or i == len(copy) - 1:
            final_text = final_text + "#" + "\n"
        else:
            final_text = final_text + copy[i]
    print(final_text)
    print("\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()
    if new_file != "":
        print(f"Saving data to {new_file}")
        try:
            file_name: str = new_file
            new_file: typing.IO = open(new_file, "w")
            new_file.write(final_text)
            new_file.close()
            print(f"Data saved in file '{file_name}'.")
        except (OSError, ValueError) as e:
            sys.stderr.write(f"[STDERR] Error opening file "
                             f"'{new_file}': {e}\nData not saved.")
    else:
        print("Not saving data")


if __name__ == "__main__":
    main()
