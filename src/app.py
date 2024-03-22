from handle_path import *

if __name__ == "__main__":
    for old_image_path in images_path.get_all_images_directory():
        logging.info(f"------------{old_image_path}-------------")
        list__image_name = convert_to_list(old_image_path)
        new_image_folder = create_image_path(list__image_name)
        image_name = create_image_name(old_image_path)
        image_name = check_if_image_is_already_in_path(image_name, new_image_folder)
        new_image_path = os.path.join(new_image_folder, image_name) 
        move_image_to_new_path(old_image_path, new_image_path)
        logging.info(f"Moved image: {old_image_path} successfully \n")