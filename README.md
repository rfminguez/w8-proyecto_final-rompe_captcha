# Introducción
Un `captcha` es una herramienta que se utiliza para distinguir si un usuario es una máquina o un humano. Habitualmente son imágenes que ocultan un texto deformado, desplazado y al que se añade ruido, que es relativamente fácil de intepretar para un ser humano pero muy difícil para una máquina usando herramientas OCR.

![ejemplo](/static/images/8J90.png)

Este es el proyecto final para el bootcamp de Data de IronHack. El objetivo es extraer el texto oculto en imágenes `captcha` usando técnicas de análisis de imagen y Machine Learning (concretamente Redes Neuronales Convolucionales). 

Se trata de una PoC, limitada en el alcance para reducir la complejidad del problema y hacerla abarcable en una semana:
* resolver captchas de 4 caracteres.
* letras mayúsculas y números entre 1 y 9 (el "0" es difícil de distinguir de una "O" mayúscula incluso para el ojo humano). En total son 36 caracteres. 
* imágenes generadas con el módulo `capcha` de Python (`https://pypi.org/project/captcha/`).

Este proyecto está dividido en varias partes:

# Preparación del Set de Datos y Entrenamiento de la Red Neuronal
Para generar el set de datos (i.e. el conjunto de `captchas`) que usaré para entrenar el modelo de Machine Learning) he creado los siguientes scripts que están dentro del directorio `src`:

* `genera_captchas_dataset.py`: genera un conjunto de captchas de 4 letras. Puede recibir como argumento:
  * `-n`: número de `captchas` que va a generar.
  * `-d`: directorio donde se van a guardar.
 
* `extrae_letras.py`: a partir de un conjunto de `captchas` guardados en un directorio extrae para cada uno cuatro regiones (una por cada carácter). Puede recibir estos argumentos.
  * `-i`: directorio donde están los `captchas`.
  * `-o`: directorio donde se guardan las letras extraídas.
 
El proceso de crear el set de datos de entrenamiento consta de dos pasos:
1. generar el set de captchas. Por ejemplo, en este caso creo 10.000 captchas:
```
cd src
python3 genera_captchas_dataset.py -n 10000 -d ../input/captchas_dataset/train_data/
```

2. extraer los caracteres (regiones) de todos esos captchas:
```
cd src
python3 extrae_letras.py -i ../input/captchas_dataset/train_data/ -o ../input/letter_dataset/training/
```

El código de estos scripts está separado en módulos que también están en el directorio `src`:
* `extrae_letras_toolbox.py`: contiene funciones para extraer las regiones de cada `captcha` que contienen las letras.
* `img_toolbox.py`: contiene funciones para trabajar con imágenes (usando sobre todo la librería `opencv`.
* `mi_captcha.py`: contiene la clase *Captcha* que se instancia en `genera_captchas_dataset.py`.
# Entrenamiento del Modelo de Machine Learning
En el Jupyter Notebook `02 - Entrenamiento.ipynb` está el proceso de entrenamiento del modelo de Redes Neuronales.

En resumen este modelo consta de:
* 2 capas convolucionales de 32 y 64 nodos.
* 1 capa intermedia de 1024 nodos.
* 1 capa de salida con 36 nodos (uno por cada posible carácter dentro de los `captchas`).

Usa como set de datos los caracteres extraídos de los `captchas` generados con los scripts descritos arriba.
# Predicciones
Extracción de las letras de uno o varios `captchas` que no están en el set de entrenamiento.

Esto se hace dentro del Jupyter Notebook `03 - Captcha Text Prediction.ipynb`.

Para mejorar la legibilidad de estos notebooks he separado parte del código en un módulo dentro del directorio `src`: 
* `predictions_toolbox.py`
# TO-DOs
Como he comentado este proyecto está limitado y tiene muchos áreas donde se puede mejorar. La más importante:
* Mejorar la precisión del modelo. En estos momentos resuelve correctamente aproximadamente el 50% de los captchas de test. Se me ocurre que esto puede mojorar aumentando los datos de entrenamiento o ajustando el algoritmo de Machine Learning usado.

Una vez hecho esto, creo que sería interesante añadir nuevas funcionalidades:
* No limitarla a una sola librería generadora de `captchas`. Ahora es muy dependiente y puede decirse que está *sobre-entrenado* para el módulo `captcha` de python. Tendría que probar a aumentar el set de datos de entrenamiento incorporando imágenes generadas con otras herramientas y probar si las predicciones mejoran.
* No limitarla el número de caracteres. Habría que pensar una técnica para distinguir el número de caracteres que puede haber en un captcha. Por ejemplo, en este pdf comentan un par de técnicas que tendría que estudiar: [http://ceur-ws.org/Vol-1885/93.pdf].
* Crear un script o un interfaz para automatizara la descarga y procesamiento de `captchas` usando *web scraping*.
# Enlaces
Para este proyecto he utilizado las siguientes fuentes de información:
* Otros proyectos similares:

https://www.kaggle.com/kanncaa1/convolutional-neural-network-cnn-tutorial

https://www.kaggle.com/fournierp/captcha-version-2-images\?

https://www.kaggle.com/aakashnain/building-a-captcha-ocr-in-tf2-0

https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710

https://github.com/JackonYang/captcha-tensorflow

https://github.com/scnuhealthy/cnn_keras_captcha

https://www.novatec-gmbh.de/en/blog/deep-learning-for-end-to-end-captcha-solving/
* Artículos:

https://medium.com/towards-artificial-intelligence/breaking-captcha-using-machine-learning-in-0-05-seconds-9feefb997694

http://ceur-ws.org/Vol-1885/93.pdf
* Documentación OpenCV y pytesseract:

https://nanonets.com/blog/ocr-with-tesseract/

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
