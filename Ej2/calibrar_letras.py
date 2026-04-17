import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from helpers import encontrarRespuestas, bordesExamen, extraerCaracteristicasLetra

# Carga la imagen del examen 4, que tiene balanceadas la cantidad de respuestas.
img = cv2.imread("./Ej2/examen_4.png", cv2.IMREAD_GRAYSCALE)

respuestas_4 = {
    1: 'B', 2: 'C', 3: 'D', 4: 'B', 5: 'A', 
    6: 'A', 7: 'C', 8: 'D', 9: 'B', 10: 'A'
}

# Lista para guardar las características
caracteristicas = []

bordes = bordesExamen(img)

for e in range(1, 11):
    (l, t), (r, b) = bordes[e]
    ejercicio = img[t:b, l:r]
    respuestas = encontrarRespuestas(ejercicio)
    
    # Solo calibramos si detectó exactamente 1 respuesta
    if len(respuestas) == 1:
        x, y, w, h, area = respuestas[0]
        letra = respuestas_4[e]
        # Recortamos la letra con un margen
        margen = 2
        letra_roi = ejercicio[max(0, y-margen) : y+h+margen, max(0, x-margen) : x+w+margen]
    
        # Sacamos los agujeros y el área del agujero más grande
        agujeros, area_agujero = extraerCaracteristicasLetra(letra_roi)
        caracteristicas.append((letra, w, h, area, agujeros, area_agujero))
        print(e,letra,w,h,area, agujeros, area_agujero)
