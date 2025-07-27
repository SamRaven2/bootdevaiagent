import os

def is_valid_directory(working_directory, directory):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_final_directory = os.path.abspath(os.path.join(absolute_working_directory, directory))
    if os.path.isdir(absolute_final_directory):
        return absolute_final_directory.startswith(absolute_working_directory)
    else:
        raise Exception("Given path is not a directory")