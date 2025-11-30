

import os


def read_all_lines(file_path):
    """Reads all lines from a file and returns them as a list.

    Args:
        file_path (str): The path to the file to be read."""
    lines = []
    for file_name in os.listdir(file_path):
        full_path = os.path.join(file_path, file_name)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as file:
                lines.extend(file.readlines())
    return lines