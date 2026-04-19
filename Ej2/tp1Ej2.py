import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from helpers import *


respuestasCorrectas = ['C', 'B', 'A', 'D', 'B', 'B', 'A', 'B', 'D', 'D']

# Procesamos los exámenes del 1 al 5
for n in range(1, 6):
    print(f"\n===== examen_{n}.png =====")
    img = cv2.imread(f"./Ej2/examen_{n}.png", cv2.IMREAD_GRAYSCALE)
    bordes = bordesExamen(img)

    # Validamos los campos del encabezado
    (l, t), (r, b) = bordes[0]
    encabezado = img[t:b, l:r]
    estado_encabezado = validarEncabezado(encabezado)
    print(f"Name: {estado_encabezado['Name']}")
    print(f"Date: {estado_encabezado['Date']}")
    print(f"Class: {estado_encabezado['Class']}")

    aciertos = 0
    for e in range(1, 11):
        (l, t), (r, b) = bordes[e]
        ejercicio = img[t:b, l:r]

        respuesta = identificarRespuestas(ejercicio)

        if respuesta == respuestasCorrectas[e-1]:
            estado = "OK"
            aciertos += 1
        else:
            estado = "MAL"

        print(f"Pregunta {e}: {estado}")
    if aciertos >= 6:
        print(f"Resultado: APROBADO ({aciertos} aciertos)")
    else:        
        print(f"Resultado: DESAPROBADO ({aciertos} aciertos)")