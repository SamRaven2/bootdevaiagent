import os

def validate_path(working_directory, relative_path):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_final_path = os.path.abspath(os.path.join(absolute_working_directory, relative_path))
    if absolute_final_path.startswith(absolute_working_directory):
        return absolute_final_path
    else:
        raise Exception(f"Final path is outside given working directory")