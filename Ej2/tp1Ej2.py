import cv2
import numpy as np
import matplotlib.pyplot as plt


def bordesExamen(img):
    th=192

    img_th=img<th

    img_cols = np.sum(img_th,0)
    img_rows = np.sum(img_th,1)

    alto_imagen, ancho_imagen = img.shape

    th_col = int(0.75*alto_imagen)
    th_row = int(0.75*ancho_imagen)

    img_cols_th = img_cols>th_col
    img_rows_th = img_rows>th_row

    left = []
    top = []
    right = []
    bottom = []

    for i in range(0,len(img_cols_th)-1):
        left_col = img_cols_th[i]
        right_col = img_cols_th[i+1]
        if left_col != right_col:
            if left_col and not right_col:
                left.append(i+1)
            else:
                right.append(i)


    for i in range(0,len(img_rows_th)-1):
        top_row = img_rows_th[i]
        bottom_row = img_rows_th[i+1]
        if top_row != bottom_row:
            if top_row and not bottom_row:
                top.append(i+1)
            else:
                bottom.append(i)

    # Bordes de cada recuadro, empezando por el encabezado
    bordes = {
        0:((0,0),(ancho_imagen,bottom[0]))
        }
    
    # Eliminamos las coordenadas fuera de los ejercicios
    del right[0]
    del bottom[0]
    del left[1]
    del right[1]
    del top[-1]
    del left[-1]

    for e in range(0,10):
        i = e%5
        j = e//5
        bordes[e+1]=((left[j],top[i]),(right[j],bottom[i]))

    return bordes


# Carga la imagen de un examen del ejercicio.
img = cv2.imread("./Ej2/examen_3.png", cv2.IMREAD_GRAYSCALE)

bordes = bordesExamen(img)

(l,t), (r,b)=bordes[5]
ejercicio3=img[t:b,l:r]

# Se muestran las tres imagenes para comparar.
plt.figure()
plt.title('Examen 3, Ejercicio 5')
plt.imshow(ejercicio3, cmap = 'gray')
plt.show()