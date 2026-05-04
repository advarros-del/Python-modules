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
        copy: typing.IO = f.read()
        print(copy)
        f.close()
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.")
    except (OSError, ValueError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    print("\nTransform data:\n---\n")
    final_text: str = ""
    for i in range(len(copy)):
        if copy[i] == "\n" or i == len(copy) - 1:
            final_text = final_text + "#" + "\n"
        else:
            final_text = final_text + copy[i]
    print(final_text)
    print("\n---")
    new_file = input("Enter new file name (or empty): ")
    if new_file != "":
        if not new_file.endswith(".txt"):
            new_file = new_file + ".txt"
        print(f"Saving data to {new_file}")
        file_name: str = new_file
        new_file: typing.IO = open(new_file, "w")
        new_file.write(final_text)
        new_file.close()
        print(f"Data saved in file '{file_name}'.")
    else:
        print("Not saving data")


if __name__ == "__main__":
    main()
