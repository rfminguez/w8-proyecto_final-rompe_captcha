from imutils import paths
import imutils
import cv2
import numpy as np
import os


def resize_to_fit(image, width, height):
    (h, w) = image.shape[:2]

    # si el ancho es más que el alto se hace resize por anchura
    if w > h:
        image = imutils.resize(image, width=width)
    else:
        image = imutils.resize(image, height=height)

    # ajusto el tamaño
    padding_width = (width - image.shape[1]) // 2
    padding_height = (height - image.shape[0]) // 2
    image = cv2.copyMakeBorder(image, padding_height, padding_height, padding_width, padding_width, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    return image


def get_image_from_file(image_file):
    return cv2.imread(image_file)


def image_to_bnw(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize_image(image, height, width):
    return resize_to_fit(image, height, width)


def add_third_dimension(image):
    return np.expand_dims(image, axis=2)


def get_preprocessed_letter_image(image_file):
        image = get_image_from_file(image_file)
        image = image_to_bnw(image)
        image = resize_image(image, 20, 20)

        # Sin esto Keras no funciona
        image = add_third_dimension(image)
        
        return image

def get_letter_label_from_folder_name(image_file):
    return image_file.split(os.path.sep)[-2]
    

def get_letters_dataset(letter_images_folder):
    data = []
    labels = []

    for image_file in paths.list_images(letter_images_folder):
        letter_image = get_preprocessed_letter_image(image_file)
        letter_label = get_letter_label_from_folder_name(image_file)
        
        data.append(letter_image)
        labels.append(letter_label)

    return data, labels
