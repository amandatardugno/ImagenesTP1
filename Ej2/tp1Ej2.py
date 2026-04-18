import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from helpers import *


# Carga la imagen de un examen del ejercicio.
img = cv2.imread("./Ej2/examen_2.png", cv2.IMREAD_GRAYSCALE)

bordes = bordesExamen(img)

for e in range(1, 11):
    (l, t), (r, b) = bordes[e]
    ejercicio = img[t:b, l:r]

    respuesta=identificarRespuestas(ejercicio)
        
    # Mostramos el ejercicio
    print(f"Respuesta del ejercicio {e}: {respuesta}")