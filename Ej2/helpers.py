import cv2
import numpy as np

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

    # Agregamos un padding por si el borde no esta tan bien cortado
    p=2

    for e in range(0,10):
        i = e%5
        j = e//5
        bordes[e+1]=((left[j]+p,top[i]+p),(right[j]-p,bottom[i]-p))

    return bordes

def encontrarRespuestas(img):
    # Umbralizamos e invertimos
    # Lo negro pasa a ser blanco (255) y el fondo blanco pasa a negro (0)
    # Esto lo hacemos para que funcione buscar las componentes conectadas
    _, img_th = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

    # Etiquetamos las componentes conectadas
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_th, 8, cv2.CV_32S)

    # Buscamos la línea donde se encuentra la respuesta
    # Ignoramos el índice 0 porque es el fondo (background)
    linea=[]
    for i in range(1, num_labels):
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]

        # Si el ancho es más del triple que el alto, debe ser una línea y terminamos este bucle
        if w > (h * 3):
            linea=[x,y,w,h]
            break

    if not linea:
        print("No encontré la línea de respuesta")
        exit()
    
    respuestas = []

    for i in range(1, num_labels):
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]

        xl, yl, wl, hl = linea

        # Eliminamos ruido (píxeles sueltos o puntos)
        if area < 5:
            continue

        # La respuesta debería estar sobre la linea de respuesta
        # Asumimos que entonces una letra para abajo de la respuesta,
        # debería intersecar a la línea
        if x > xl and x < xl + wl and yl < y + 2*h and yl > y+h:
            respuestas.append((x, y, w, h, area))

    return respuestas

def extraerCaracteristicasLetra(roi_letra):
    """
    Recibe la imagen binarizada de una sola letra recortada.
    Devuelve (cantidad_agujeros, area_agujero_max)
    """
    _, roi_letra = cv2.threshold(roi_letra, 150, 255, cv2.THRESH_BINARY_INV)

    # Buscamos los contornos 
    contours, hierarchy = cv2.findContours(roi_letra, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # Por si no llegara a detectar contornos, sale
    if hierarchy is None:
        return 0, 0

    jerarquia = hierarchy[0] # hierarchy devuelve un array de shape (1, N, 4)
    
    cantidad_agujeros = 0
    area_agujero_max = 0
    
    # jerarquia[i] = [Next, Previous, First_Child, Parent]
    for i, contorno in enumerate(contours):
        padre = jerarquia[i, 3] # El índice 3 es el 'Parent'
        
        if padre != -1:
            # Si tiene un padre (Parent != -1), significa que es un contorno interno (un agujero)
            area_hijo = cv2.contourArea(contorno)
            # Filtramos por si detectó un píxel suelto adentro como agujero
            if area_hijo > 3: 
                cantidad_agujeros += 1
            if area_hijo>area_agujero_max:
                area_agujero_max=area_hijo
                
    return cantidad_agujeros, area_agujero_max