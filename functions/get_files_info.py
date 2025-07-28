import os

from functions.validate_path import validate_path

def get_files_info(working_directory, directory="."):
    
    try:
        absolute_final_path = validate_path(working_directory, directory)
    except Exception:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_final_path):
        return f'Error: "{directory}" is not a directory'

    files_list = os.listdir(absolute_final_path)
    output_strings = []
    for file in files_list:
        size = os.path.getsize(os.path.join(absolute_final_path, file))
        is_dir = os.path.isdir(os.path.join(absolute_final_path, file))
        output_strings.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(output_strings)