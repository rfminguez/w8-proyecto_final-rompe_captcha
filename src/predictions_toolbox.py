import src.extrae_letras_toolbox as etb
from imutils import paths
import pickle
import cv2
import numpy as np
from keras.models import load_model
from src.img_toolbox import resize_to_fit


from matplotlib import pyplot as plt


def plot_individual_image(image, letters_list):
    plt.figure()
    
    text = "Predicción: " + str(letters_list)
    plt.gcf().text(1, 0.5, text, fontsize=14, bbox=dict(facecolor='red', alpha=0.5))
    
    plt.imshow(image)
    plt.show;

    
def transform_captcha_image(image):
    # Hago las mismas transformaciones que en el script `extraer_letras.py` y el notebook `01 - Creacion Dataset Letras`:
    image_bnw = etb.image_to_bnw(image.copy())
    dilation_image = etb.apply_dilation(image_bnw)
    erosion_image = etb.apply_erosion(dilation_image)
    denoise_image = etb.apply_denoise(erosion_image)
    thresholded_image = etb.apply_thresholding(denoise_image)

    return thresholded_image


def predict(image, regions, model, labels):
    result = []
    
    # Las regiones están ordenadas por la coordenada X (la de la izquierda contienen la primera letra)
    # Recorro todas esas regiones (deberían ser 4 regiones tras el paso anterior).
    for region in etb.get_sorted_regions_by_coord_x(regions):
        x, y, w, h = region

        # Corto una región que contiene una letra
        letter_image = image[y:y + h, x:x + w]
        # Importante: 
        # La predicción se hace sobre la imagen transformada (no sobre la original).
        # Ten en cuenta que los datos de entrenamiento (las letras) también han pasado por este proceso de transformación
        # que quitar en lo posible el ruido que incorpora el algoritmo de generación de capchas .

        # Redimensiono la región a 20x20 pixels (igual que los datos de entrenamiento)
        letter_image = resize_to_fit(letter_image, 20, 20)

        # Convierto cada imagen de letra en una lista de 4 dimensiones. Sin esto Keras no funciona.
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        # Uso el modelo para hacer predicciones
        prediction = model.predict(letter_image)

        # Con la predicción busco en las labels (que codifiqué en one-hot-encoding) a que letra corresponde
        letter = labels.inverse_transform(prediction)[0]
        
        # Y añado la predicción al resultado
        result.append(letter)

    return result
