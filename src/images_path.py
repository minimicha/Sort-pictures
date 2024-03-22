import os
import logging

from functools import reduce

from settings import SOURCE_FILE

logging.basicConfig(level=logging.INFO)


def get_all_directories_recursive(directory_name: str = SOURCE_FILE) -> list:
    """
    Recursively scan the specified directory and its subdirectories to
    retrieve a list of all existing directories.

    Parameters:
    - directory_name (str): The path to the directory to be scanned. Defaults to SOURCE_FILE.

    Returns:
    - list: A list of directory paths.
    """
    # List comprehension to get subfolders using os.scandir
    sub_folders = [
        folder.path for folder in os.scandir(directory_name) if folder.is_dir()
    ]

    # Recursively scan subdirectories and create a new list
    new_sub_folders = []
    for sub_directory in sub_folders:
        new_sub_folders.extend(get_all_directories_recursive(sub_directory))

    # Extend the original list with the new directories and return it
    sub_folders.extend(new_sub_folders)

    # Return the list of directories, including the current one
    return sub_folders if sub_folders else [directory_name]


def get_all_images_directory() -> list:
    list_of_directories = []
    for folder_path in get_all_directories_recursive():
        logging.info(f"Getting image directories from location: {folder_path}")
        list_of_directories.append(
            [
                os.path.join(folder_path, file)
                for file in os.listdir(folder_path)
                if os.path.isfile(os.path.join(folder_path, file))
            ]
        )
    list_of_directories = [x for x in list_of_directories if x]
    single_list = reduce(lambda x, y: x + y, list_of_directories)
    return single_list


def get_all_image_path(path: str) -> list:
    tree = []
    for root, _, files in os.walk(path):
        tree.append(root)
        for f in files:
            tree.append(os.path.join(root, f))
    return tree
