# Librerías a utilizar:
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Función de ecualizado de histograma local.
def ecualizacionHistogramaLocal(img, ventana):
    """
    img: Imagen de entrada (grayscale).
    ventana: Tupla con tamaño de ventana (debe ser impar, ej: (15, 15)).
    Devuelve: Imagen con ecualizado de histograma local.
    """

    # Obtiene las dimensiones de la imagen y la ventana
    alto_imagen, ancho_imagen = img.shape
    alto_ventana, ancho_ventana = ventana
    
    # Inicializo la imagen de salida como una copia de la imagen original.
    img_salida = img.copy()
    
    # Calculamos el offset de la ventana para el centrado
    off_vertical = alto_ventana // 2
    off_horizontal = ancho_ventana // 2
    
    # Aplicamos padding para manejar los bordes (reflejando la imagen)
    img_pad = cv2.copyMakeBorder(img, off_vertical, off_vertical, off_horizontal, off_horizontal, cv2.BORDER_REFLECT)
    
    # Recorremos cada píxel de la imagen original
    for i in range(alto_imagen):
        for j in range(ancho_imagen):
            # Extraemos la vecindad (ROI) usando las coordenadas con padding
            # La ventana está centrada en (i + off_vertical, j + off_horizontal) en la imagen con pad
            roi = img_pad[i : i + alto_ventana, j : j + ancho_ventana]
            
            # Ecualizamos la ventana
            roi_equalizada = cv2.equalizeHist(roi)
            
            # El valor del píxel central de la ventana ecualizada (i + off_vertical, j + off_horizontal)
            # es el nuevo valor para nuestro píxel (i, j)
            img_salida[i, j] = roi_equalizada[off_vertical, off_horizontal]
            
    return img_salida

# Carga la imagen con detalles escondidos del ejercicio.
imagen_con_detalles_escondidos = cv2.imread('./Ej1/Imagen_con_detalles_escondidos.tif', cv2.IMREAD_GRAYSCALE)

# Se realiza un ecualizado de histograma a la imagen, pero sobre la imagen completa.
imagen_ecualizada = cv2.equalizeHist(imagen_con_detalles_escondidos)

# Se utiliza la función creada para hacer el ecualizado de histograma local.
imagen_ecualizada_local = ecualizacionHistogramaLocal(imagen_con_detalles_escondidos, (21, 21))

# Se muestran las tres imagenes para comparar.
plt.subplot(131)
plt.title('Sin ecualizar')
plt.imshow(imagen_con_detalles_escondidos, cmap = 'gray')

plt.subplot(132)
plt.title('Ecualizado Global')
plt.imshow(imagen_ecualizada, cmap = 'gray')

plt.subplot(133)
plt.title('Ecualizado local')
plt.imshow(imagen_ecualizada_local, cmap = 'gray')

plt.show()