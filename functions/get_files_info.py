import os

from functions.is_valid_directory import is_valid_directory

def get_files_info(working_directory, directory="."):
    try:
        if not is_valid_directory(working_directory, directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception:
        return f'Error: "{directory}" is not a directory'

    absolute_path = os.path.abspath(os.path.join(working_directory, directory))

    files_list = os.listdir(absolute_path)
    output_strings = []
    for file in files_list:
        size = os.path.getsize(os.path.join(absolute_path, file))
        is_dir = os.path.isdir(os.path.join(absolute_path, file))
        output_strings.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(output_strings)