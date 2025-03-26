from pathlib import Path
from colorama import Fore, init
import sys
import os


def show_folder_content(path, space: int = 0):
    if len(sys.argv) != 2:
        print(f"Arguments are written incorrectly{Fore.RED}{error}{Fore.RESET}")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f"Path does not exis{Fore.RED}{error}{Fore.RESET}")
        sys.exit(1)

    if not os.path.isdir(sys.argv[1]):
        print(f"Path is not a directory{Fore.RED}{error}{Fore.RESET}")
        sys.exit(1)
    try:
        for path in path.iterdir():
            spaces = space * 4 * ' '
            entity_name = Path(path).name
            if path.is_dir():
                print(f"{spaces}{Fore.BLUE}{entity_name}/{Fore.RESET}")
                show_folder_content(path, space + 1)
            elif path.is_file():
                print(f"{spaces}{Fore.GREEN}{entity_name}{Fore.RESET}")
            else:
                print(f"Unknown path or entity type")
                sys.exit(1)
    except Exception as error:
        print(error)
        return None


if __name__ == '__main__':
    init() 
    orig_path = Path(sys.argv[1])
    show_folder_content(orig_path)
    
    