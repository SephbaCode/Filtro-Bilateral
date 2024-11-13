import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *

#abrir un selector de archivos para cargar un archivo jpg desde el sistema de archivos

#agrega un try para que si no se selecciona un archivo no se caiga el programa
try:
    image_path = 'image_test/test_1_puente.jpg'
    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convertir la imagen a RGB (OpenCV usa BGR por defecto)

    # Aplicar el filtro bilateral
    # Los parámetros son:
    # - d: Diámetro del área de píxeles a considerar (tamaño del filtro).
    # - sigmaColor: Fuerte diferencia de color que se toma en cuenta para el suavizado.
    # - sigmaSpace: Distancia en el espacio que se toma en cuenta para el suavizado.
    filtered_image = cv2.bilateralFilter(image_rgb, d=15, sigmaColor=50, sigmaSpace=50)

    # Mostrar la imagen original y la filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image)
    plt.title('Imagen con Filtro Bilateral')
    plt.axis('off')

    plt.show()

except:
    print("No se selecciono un archivo")
    exit()

