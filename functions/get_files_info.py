import os

def get_files_info(working_directory, directory="."):
    
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if  os.path.isfile(absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    files_list = os.listdir(absolute_path)
    output_strings = []
    for file in files_list:
        size = os.path.getsize(os.path.join(absolute_path, file))
        is_dir = os.path.isdir(os.path.join(absolute_path, file))
        output_strings.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(output_strings)