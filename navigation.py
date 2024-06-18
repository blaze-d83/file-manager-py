import os

def get_directory_contents(path):
    """Returns a list of files and directories in the given path."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {e}"]

def navigate_down(current_path, directory):
    """Navigates into the selected directory if it's a valid directory."""
    new_path = os.path.join(current_path, directory)
    if os.path.isdir(new_path):
        return new_path
    return current_path

def navigate_up(current_path):
    """Navigates up to the parent directory."""
    return os.path.dirname(current_path)

