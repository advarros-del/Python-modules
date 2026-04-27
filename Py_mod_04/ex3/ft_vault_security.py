def secure_archive(archive_path: str,
                   binary: int, str: str) -> tuple[bool, str]:
    if binary == 0:
        try:
            with open(archive_path, "r") as f:
                content:str = f.read()
        except FileNotFoundError as e:
            return (False, f"{e}")
        except PermissionError as e:
            return (False, f"{e}")
        return (True, content)
    else:
        try:
            with open(archive_path, "w") as f:
                f.write(str)
        except PermissionError as e:
            return (False, f"{e}")
        return (True, "Content successfully written to file")
            
    
    
def main() -> None:    
    print("=== Cyber Archive Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result:tuple[bool, str] = secure_archive("/non/existent/file", 0, "")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("inaccessible_file.txt", 0, "")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", 0, "")
    print(f"{result}\n")
    print("Using 'secure_archive' to write previous content to a file:")
    string: str = result[1]
    result = secure_archive("secured_fragment.txt", 1, string)
    print(f"{result}")
    

if __name__ == "__main__":
    main()
    