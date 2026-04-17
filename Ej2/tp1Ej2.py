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

    respuestas=encontrarRespuestas(ejercicio)
        
    # Mostramos el ejercicio
    plt.figure(figsize=(4, 2))
    plt.imshow(ejercicio, cmap='gray')
    plt.title(f'Ejercicio {e} | Respuestas detectadas: {len(respuestas)}')
    ax = plt.gca()
    
    # con rectángulos en las respuestas detectadas
    for (x, y, w, h, _) in respuestas:
        rect = patches.Rectangle((x, y), w, h, linewidth=1.5, edgecolor='red', facecolor='none')
        ax.add_patch(rect)
        
    plt.axis('off')
    plt.show()