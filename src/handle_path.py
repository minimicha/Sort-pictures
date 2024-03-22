import os
import images_path
import logging
import shutil

from PIL import Image

from src.settings import DESTINATION_FILE


logging.basicConfig(level=logging.INFO)


def get_image_date(path: str) -> str:
    image = Image.open(path)
    exif = image._getexif()
    if not exif:
        raise Exception("Image {0} does not have EXIF data.".format(path))
    try:
        date = exif[36867]
        logging.info(f"image called {image.filename} was created on {date}")
    except Exception as e:
        print(exif[34665])
        raise e
    return date


def convert_to_list(path: str) -> list:
    try:
        # date time
        return get_image_date(path).split()[0].split(":")[::-1]
    except Exception as e:
        raise e


def create_image_name(path: str) -> str:
    try:
        return "_".join(convert_to_list(path)) + "_001" + ".jpg"
    except Exception as e:
        raise e


def create_image_path(list__image_name: list) -> str:
    image_path = os.path.join(
        DESTINATION_FILE, f"{list__image_name[2]}", f"{list__image_name[1]}"
    )
    logging.info(f"Image needs to be moved to {image_path}")
    try:
        os.makedirs(image_path)
        return os.makedirs(image_path)
    except FileExistsError:
        return image_path
    except Exception as e:
        raise e


def move_image_to_new_path(old_image_path: str, new_image_path: str) -> None:
    try:
        shutil.copyfile(old_image_path, new_image_path)
    except Exception as e:
        raise e


def check_if_image_is_already_in_path(image_name: str, path: str) -> str:
    new_path = os.path.join(path, image_name)
    image_as_list = image_name.split(".")[0].split("_")
    if os.path.isfile(new_path):
        while os.path.isfile(new_path):
            image_as_list = image_name.split(".")[0].split("_")
            new_number = "%03g" % (int(image_as_list[-1]) + 1)
            image_name = "_".join(image_as_list[:-1]) + "_" + new_number + ".jpg"
            new_path = os.path.join(path, image_name)
        return image_name
    else:
        return "_".join(image_as_list) + ".jpg"
