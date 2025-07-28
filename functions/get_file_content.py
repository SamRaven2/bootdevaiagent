import os
from functions.validate_path import validate_path
import config

def get_file_content(working_directory, file_path):
    try:
        absolute_file_path = validate_path(working_directory, file_path)
    except Exception as e:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(absolute_file_path, "r") as f:
        file_content_string = f.read(config.MAX_CHARACTERS)

    if os.path.getsize(absolute_file_path) > config.MAX_CHARACTERS:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string