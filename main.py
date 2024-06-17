import os
import shutil

current_dir = os.getcwd()
cursor_index = 0


def list_files_and_dirs(path):
    with os.scandir(path) as entries:
        files_and_dirs = [entry.name for entry in entries]
    return files_and_dirs


def change_dir(new_path):
    global current_dir
    try:
        os.chdir(new_path)
        current_dir = os.getcwd()
    except FileNotFoundError:
        print("Directory not found.")


def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")


def navigation_cursor(key):
    global cursor_index
    files_and_dirs = list_files_and_dirs(current_dir)
    max_index = len(files_and_dirs) - 1

    if key == "j":
        cursor_index = min(cursor_index + 1, max_index)
    elif key == "k":
        cursor_index = min(cursor_index - 1, 0)
    elif key == "l":
        if os.path.isdir(files_and_dirs[cursor_index]):
            change_dir(os.path.join(current_dir, files_and_dirs[cursor_index]))
            cursor_index = 0
    elif key == "h":
        if current_dir != "/":
            parent_dir = os.path.dirname(current_dir)
            change_dir(parent_dir)
            cursor_index = 0


while True:
    files_and_dirs = list_files_and_dirs(current_dir)
    max_index = len(files_and_dirs) - 1
    print(f"Current Directory: {current_dir}")

    for i, item in enumerate(files_and_dirs):
        if i == cursor_index:
            print(f"> {item}")
        else:
            print(f"  {item}")

    command = input("Enter ('j' , 'k', 'l', 'h', 'exit'):").strip()

    if command == "j":
        navigation_cursor("j")
    elif command == "k":
        navigation_cursor("k")
    elif command == "l":
        navigation_cursor("l")
    elif command == "h":
        navigation_cursor("h")
    elif command.startswith("cp"):
        parts = command.split()
        if len(parts) == 3:
            copy_file(parts[1], parts[2])
    elif command == "exit":
        break
    else:
        print("Invalid command.")
