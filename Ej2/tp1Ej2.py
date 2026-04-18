import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from helpers import *


# Carga la imagen de un examen del ejercicio.
img = cv2.imread("./Ej2/examen_2.png", cv2.IMREAD_GRAYSCALE)

respuestasCorrectas = ['C', 'B', 'A', 'D', 'B', 'B', 'A', 'B', 'D', 'D']

bordes = bordesExamen(img)

# Validamos los campos del encabezado
(l, t), (r, b) = bordes[0]
encabezado = img[t:b, l:r]
estado_encabezado = validarEncabezado(encabezado)
print(f"Name: {estado_encabezado['Name']}")
print(f"Date: {estado_encabezado['Date']}")
print(f"Class: {estado_encabezado['Class']}")

for e in range(1, 11):
    (l, t), (r, b) = bordes[e]
    ejercicio = img[t:b, l:r]

    respuesta = identificarRespuestas(ejercicio)

    if respuesta == respuestasCorrectas[e-1]:
        estado = "OK"
    else:
        estado = "MAL"

    print(f"Pregunta {e}: {estado}")