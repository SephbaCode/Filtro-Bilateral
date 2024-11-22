import cv2  # Para el filtro bilateral de la librería para COMPARACIÓN
import matplotlib.pyplot as plt  # Para mostrar las imágenes lado a lado
import numpy as np
import math
from tkinter import Tk, filedialog
import time

# Función gaussiana para el filtro espacial
def gaussian(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2 * sigma**2))

def bilateral_filter(image, diameter, sigma_spatial, sigma_intensity):
    # Convertir la imagen a float32 para evitar desbordamientos
    
    image = image.astype(np.float32)
    rows, cols = image.shape
    new_image = np.zeros_like(image, dtype=np.float32)
    
    half_diameter = diameter // 2  # Tamaño de la mitad de la ventana
    
    # Recorrer cada píxel de la imagen
    for i in range(rows):
        for j in range(cols):
            # Inicializar el acumulador de pesos y el valor filtrado
            Wp = 0
            filtered_intensity = 0
            
            # Recorrer la ventana de la vecindad
            for k in range(-half_diameter, half_diameter + 1):
                for l in range(-half_diameter, half_diameter + 1):
                    ni = i + k  # Índice del píxel vecino en la fila
                    nj = j + l  # Índice del píxel vecino en la columna
                    
                    # Verificar que el vecino esté dentro de los límites de la imagen
                    if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                        # Diferencia de intensidad
                        intensity_diff = image[ni, nj] - image[i, j]
                        
                        # Peso espacial
                        spatial_weight = gaussian(k, l, sigma_spatial)
                        
                        # Peso de intensidad con control de desbordamiento
                        intensity_weight = math.exp(-min((intensity_diff ** 2) / (2 * sigma_intensity ** 2), 700))
                        
                        # Peso total
                        weight = spatial_weight * intensity_weight
                        
                        # Acumular la contribución de este píxel vecino
                        filtered_intensity += image[ni, nj] * weight
                        Wp += weight
            
            # Normalizar y asignar el nuevo valor de intensidad al píxel
            new_image[i, j] = filtered_intensity / Wp if Wp > 0 else image[i, j]
    
    # Convertir de vuelta a uint8 para mostrar como imagen
    
    return np.clip(new_image, 0, 255).astype(np.uint8)


def select_image_file():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    file_path = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if file_path:
        return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    else:
        print("No se seleccionó ninguna imagen.")
        return None


# MAIN
print("Filtro Bilateral Manual vs OpenCV")
print("==================================")
print ("Eliga una imagen para aplicar el filtro bilateral.")
# Seleccionar y cargar la imagen
image = select_image_file()
if image is None:
    raise SystemExit("Se requiere una imagen para continuar.")

print("Imagen cargada correctamente")

print("Usar parametros prdeterminados? (diameter=5, sigma_spatial=10, sigma_intensity=25)")
print("1. Si \n2. No")
option = int(input())

if option == 1:
    # Parámetros del filtro bilateral
    diameter = 5  # Tamaño de la ventana
    sigma_spatial = 5  # Sigma para la distancia espacial
    sigma_intensity = 25  # Sigma para la diferencia de intensidad
else:
    try:
        print("Ingrese el tamaño de la ventana:")
        diameter = int(input())
        print("Ingrese el valor de sigma para la distancia espacial:")
        sigma_spatial = int(input())
        print("Ingrese el valor de sigma para la diferencia de intensidad:")
        sigma_intensity = int(input())
    except ValueError:
        raise SystemExit("Los valores ingresados no son válidos.")


# Aplicar el filtro bilateral manualmente
print("Aplicando filtro bilateral manualmente...")
start_time_manual = time.time()
filtered_manual = bilateral_filter(image, diameter, sigma_spatial, sigma_intensity)
end_time_manual = time.time()
print(f"Tiempo de ejecución del filtro bilateral manual: {end_time_manual - start_time_manual:.2f} segundos")
print("Completado")


# Aplicar el filtro bilateral usando OpenCV
print("Aplicando filtro bilateral con OpenCV...")
star_time_cv = time.time()
filtered_cv = cv2.bilateralFilter(image, diameter, sigma_intensity, sigma_spatial)
end_time_cv = time.time()
print(f"Tiempo de ejecución del filtro bilateral con OpenCV: {end_time_cv - star_time_cv:.2f} segundos")
print("Completado")

# Mostrar las imágenes en una columna usando Matplotlib
plt.figure(figsize=(6, 12))  # Ajusta el tamaño de la figura para una disposición vertical


# mostar resultados
plt.subplot(3, 1, 1)  # Primera fila, primera columna
plt.title("Imagen Original")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(3, 1, 2)  # Segunda fila, primera columna
plt.title("Filtro Bilateral Manual")
plt.imshow(filtered_manual, cmap='gray')
plt.axis('off')

plt.subplot(3, 1, 3)  # Tercera fila, primera columna
plt.title("Filtro Bilateral OpenCV")
plt.imshow(filtered_cv, cmap='gray')
plt.axis('off')

plt.tight_layout()  # Ajusta automáticamente los márgenes entre subgráficos
plt.show()
