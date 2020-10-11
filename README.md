# Proyecto Final del Bootcamp
Intento de romper captchas usando Machine Learning.

Para simplificar el problema:
- voy a limitarme a captchas de 4 caracteres alfanuméricos.
- letras mayúsculas y números entre 1 y 9 (el "0" es imposible de distinguir el "0" de una "o" mayúscula incluso para el ojo humano).
- limitado a un solo tipo de fuente (los captchas suelen utilizar distintos tipos de fuente para hacer más difícil distinguir los caracteres).

- estos captchas los generaré usando la de python
    https://pypi.org/project/captcha/


# Preparar el set de datos
Separar el captcha en 4 trozos correspondientes a los 4 caracteres.

Cada uno de esos caracteres (imágenes) para todas las imágenes seleccionadas serán con lo que se entrene la red neuronal. El objetivo es conseguir diferentes variaciones de cada letra o número.

Esto no es tan fácil como separar la imagen en trozos del mismo tamaño porque los caracteres en un captcha las letras tienen diferentes tamaños, aparecen giradas, y desplazadas en posiciones aleatorias de modo que en muchos casos se solapan.

Esto lo haré usando la librería OpenCV.


# Entrenar Algoritmo Machine Learning


# TO-DOs

- TO-DO incluir letras mayúsculas y minúsculas (algunas, como la "v", "w", "x", "y" u "o" son muy difíciles de distinguir incluso para el ojo humano). También es muy difícil distinguir "1" de "l" minúscula.
- TO-DO captchas con distintos tipos de fuentes.
- TO-DO captchas con un número variable de caracteres.
- TO-DO incluir un interfaz API y/o gráfico.

- las imágenes se guardan en el directorio `input` como gráficos .PNG, el nombre del archivo es el texto que está oculto en la imagen.
- a partir de las imágenes se separan las letras que se utilizarán como entrenamiento para una red neuronal.









--------------

Keras vs Tensorflow vs Spark:
https://www.edureka.co/blog/keras-vs-tensorflow-vs-pytorch/


TOPOLOGÍAS DE RED
VGG:
https://www.quora.com/What-is-the-VGG-neural-network

VGG es una topología de Red Neuronal propuesta por Karen Simonyan y Andrew Zisserman del Oxford Robotics Institute en el año 2014.

Esta topología consiguió muy buenos resultados en la competición  de reconocimiento de imágenes Large Scale Visual Recognition Challenge 2014.


A HOMBROS DE GIGANTES:
Howtos y tutoriales:
	https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710
	https://github.com/JackonYang/captcha-tensorflow
	https://github.com/scnuhealthy/cnn_keras_captcha
	https://www.novatec-gmbh.de/en/blog/deep-learning-for-end-to-end-captcha-solving/

OpenCV y pytesseract:
https://nanonets.com/blog/ocr-with-tesseract/

Image processing with OpenCV:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html

Proyectos Kaggle:
	https://www.kaggle.com/fournierp/captcha-version-2-images?
	https://www.kaggle.com/aakashnain/building-a-captcha-ocr-in-tf2-0
	

Artículos:
	https://medium.com/towards-artificial-intelligence/breaking-captcha-using-machine-learning-in-0-05-seconds-9feefb997694
	http://ceur-ws.org/Vol-1885/93.pdf

Basándome en estos enlaces:
	https://deepmlblog.wordpress.com/2016/01/03/how-to-break-a-captcha-system/
	https://github.com/deathlyface/recaptcha-dataset
	https://github.com/JackonYang/captcha-tensorflow

https://www.quora.com/What-is-the-VGG-neural-network
https://www.edureka.co/blog/keras-vs-tensorflow-vs-pytorch/
