# Librerías a utilizar:
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Función de ecualizado de histograma local.
def ecualizacionHistogramaLocal(img, ventana):
    """
    img: Imagen de entrada.
    ventana: Tupla con tamaño de ventana.
    Devuelve: Imagen con ecualizado de histograma local.
    """
    # Realiza una copia de la imagen original.
    copia_img = img.copy()
    # Obtiene el ancho y largo de la imagen.
    ancho_img, alto_img = copia_img.shape
    # Obtiene el ancho y largo de la ventana, pasados como parámetros.
    ancho_ventana, alto_ventana = ventana

    # Recorre la imagen en diferentes ventanas del tamaño seleccionado.
    for i in range(0, ancho_img - ancho_ventana, ancho_ventana):
        for j in range(0, alto_img - alto_ventana, alto_ventana):
            # Realiza el ecualizado de histograma en cada ventana.
            copia_img[i:i + ancho_ventana, j:j + alto_ventana] = cv2.equalizeHist(copia_img[i:i + ancho_ventana, j:j + alto_ventana])

    # Aplica medianBlur para reducir el ruido de la imagen.
    copia_img = cv2.medianBlur(copia_img, 3)

    # Devuelve la imagen nueva.
    return copia_img

# Carga la imagen con detalles escondidos del ejercicio.
imagen_con_detalles_escondidos = cv2.imread('./Imagen_con_detalles_escondidos.tif', cv2.IMREAD_GRAYSCALE)

# Se realiza un ecualizado de histograma a la imagen, pero sobre la imagen completa.
imagen_ecualizada = cv2.equalizeHist(imagen_con_detalles_escondidos)

# Se utiliza la función creada para hacer el ecualizado de histograma local.
imagen_ecualizada_local = ecualizacionHistogramaLocal(imagen_con_detalles_escondidos, (14, 14))

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