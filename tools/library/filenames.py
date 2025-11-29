import datetime
import string
import os

def generate_unique_filename(input: str, file_extension: str = None) -> str:
    """
    Generates a unique and sanitized filename based on the provided string.
    This function ensures the filename is safe for use by removing invalid characters
    and replacing spaces with underscores. It also appends the current date to the
    filename for uniqueness. Optionally, a file extension can be added.
    Args:
        s (str): The base string to generate the filename from.
        file_extension (str, optional): The file extension to append to the filename. Defaults to None.
    Returns:
        str: A unique, sanitized filename with the current date and optional file extension.
    """
    valid_characters = "-_.() %s%s" % (string.ascii_letters, string.digits)
    file_name = ''.join(c for c in input if c in valid_characters)
    file_name = file_name.replace(' ', '_')

    current_date = datetime.datetime.today()

    file_name = str(current_date.year) + "_" + str(current_date.month) + "_" + str(current_date.day) + "_" + file_name

    if file_extension is not None:
        file_name = file_name + file_extension

    file_name = file_name.lower()
    
    return file_name


def generate_not_existing_filename(file_name: str) -> str:
    """
    Generates a unique file name by appending an index to the base name 
    if a file with the given name already exists.
    Args:
        file_name (str): The desired file name, including its extension.
    Returns:
        str: A unique file name that does not already exist in the file system.
    """

    base_file_name, file_extension = os.path.splitext(file_name)
    modified_base_file_name = base_file_name
    
    index = 0
    while os.path.isfile(modified_base_file_name + file_extension):
        index = index + 1
        modified_base_file_name = base_file_name + f"_{index}"
        
    modified_file_name = modified_base_file_name + file_extension
    
    return modified_file_name


def get_absolute_path(relative_path: str) -> str:
    """
    Converts a relative file path to an absolute file path.
    Args:
        relative_path (str): The relative path to be converted.
    Returns:
        str: The absolute path corresponding to the given relative path.
    """
    
    absolute_path  = os.path.abspath(relative_path)
    return absolute_path 