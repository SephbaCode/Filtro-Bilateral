# Aplicación de Filtro Bilateral a Imágenes

Este repositorio contiene el desarrollo de un trabajo universitario sobre la **aplicación de un filtro bilateral a imágenes**. El proyecto forma parte de la asignatura de **Sistemas Lineales y Señales** y tiene como objetivo explorar técnicas de procesamiento de imágenes mediante filtros avanzados.

---

## Descripción

El **filtro bilateral** es una técnica de procesamiento de imágenes no lineal que permite suavizar una imagen mientras preserva los bordes. Esto se logra al considerar tanto la proximidad espacial como la diferencia de intensidad al calcular el nuevo valor de cada píxel.

En este proyecto se realiza:

- **Implementación del filtro bilateral:** Aplicación del filtro usando algoritmos en Python.
- **Análisis de resultados:** Comparación entre la imagen original y la imagen filtrada.
- **Casos de uso:** Aplicación en diferentes tipos de imágenes para evaluar el desempeño.

---

## Estructura del Proyecto

📂 filtro-bilateral  
├── 📁 imagenes prueba # Contiene las imágenes de prueba  
├── filtro_bilateral.py # Implementación principal del filtro   
├── README.md # Este archivo  
└── requirements.txt # Dependencias del proyecto

yaml
Copiar código

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- Librerías:
  - OpenCV
  - NumPy
  - Matplotlib

Para instalarlas, utiliza el archivo `requirements.txt`:


## Uso
  1. Clonar este repositorio:
     ```bash
     git clone https://github.com/tu-usuario/filtro-bilateral.git```
     
  2. Instalar dependencias necesarias:
     Utilizar el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt```
    
  3. Ejecutar el script principal:
     ```bash
     python src/filtro_bilateral.py```
  4. Seleccionar una Imagen para aplicar el filtro (Se puede usar alguna de la carpeta test)
  5. Esperar Resultados.
  6. El resultado se vizualizara mediante un plot, en consola de mostraran los tiempos de ejecución.

