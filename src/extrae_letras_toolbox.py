import cv2
import re
import os
import numpy as np
import datetime as dt


def get_image(file_path):
    return cv2.imread(file_path)

def get_captcha_text_from_filename(file_path):
    filename = os.path.basename(file_path)
    return re.sub(r"\.png$", "", filename)

def image_to_bnw(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_dilation(image):
    kernel = np.ones((2,2), np.uint8)
    return cv2.dilate(image, kernel, iterations=3)

def apply_erosion(image):
    kernel = np.ones((2,2), np.uint8)
    return cv2.erode(image, kernel, iterations=2)

def apply_denoise(image):
    return cv2.fastNlMeansDenoising(image, 21, 7)

def apply_thresholding(image):
    return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,2)

def smoothing_median_blur(image, max_kernel_length = 10):
    for i in range(1, max_kernel_length, 2):
        smoothed_image = cv2.medianBlur(image.copy(), i)
    return smoothed_image

def image_thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,91,2)

def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def get_area(width, height):
    return width * height

def get_regions(contours):
    regions = []
    
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Asumo que si el área de un rectángulo es menor de 300 se trata de una agrupación de puntos en vez de una letra
        if get_area(w, h) > 300:
            regions.append((x, y, w, h))

    return regions

def adjust_regions_by_number(regions, target_number_of_regions):
    while len(regions) < target_number_of_regions:
        largest_region = get_largest_region_by_area_size(regions)
        new_regions = divide_region_by_width(largest_region)
        regions += new_regions
        regions.remove(largest_region)
    return regions

def get_sorted_regions_by_area_size(regions):
    '''
    recibe:   Una lista con regiones.
              Cada región es una tupla con cuatro valores:
              - coordenada x
              - coordenada y
              - altura
              - anchura
    devuelve: la lista ordenada de región con mayor área a región con menor área 
    '''
    # Los índices 2 y 3 corresponden a altura y anchura
    return sorted(regions, key=lambda x: get_area(x[2], x[3]), reverse = True)

def get_largest_region_by_area_size(regions):
    return get_sorted_regions_by_area_size(regions)[0]

def divide_region_by_width(region):
    '''
    recibe: una tupla con cuatro valores:
            - coordenada x
            - coordenada y
            - anchura
            - altura

    devuelve: dos regiones resultado de la división de la región anterior por anchura.
    '''
    x, y, w, h = region
    half_width = w // 2
    
    result = []
    result.append((x, y, half_width, h))
    result.append((x + half_width, y, half_width, h))
    
    return result

def get_sorted_regions_by_coord_x(regions):
    return sorted(regions, key=lambda r: r[0])

def save_letter_image(image, letter, output_folder = 'input/letter_dataset/training/'):
    save_path = os.path.join(output_folder, letter)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    filename = letter + "_" + dt.datetime.now().strftime("%y%m%d_%H%M%S%fZ")

    file_path = os.path.join(save_path, f"{filename}.png")
    cv2.imwrite(file_path, image)
