# Aplicación de Filtro Bilateral a Imágenes

Este repositorio contiene el desarrollo de un trabajo universitario sobre la **aplicación de un filtro bilateral a imágenes**. El proyecto forma parte de la asignatura de **Sistemas Lineales y Señales** y tiene como objetivo explorar técnicas de procesamiento de imágenes mediante filtros avanzados.

---

## Autores
**Universidad de Cuenca**  
**Joseph Mateo Sangurima Baculima**  
joseph.sangurima@ucuenca.edu.ec  
**Lenin Santiago Anguisaca Landivar**  
lenin.anguisaca@ucuenca.edu.ec  


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
├── 📁 imagenes prueba #imágenes de prueba  
├── 📄filtro_bilateral.py # Implementación del filtro   
├── 📃README.md # Este archivo  
└── 📄requirements.txt # Dependencias del proyecto

---

## Requisitos

Antes de ejecutar el proyecto, asegúrarse de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- Librerías:
  - OpenCV
  - NumPy
  - Matplotlib

Para instalarlas, utilizar el archivo `requirements.txt`.  
Estas serán necesarias para realizar comparacion entre el filtro manual y el de libreria.

## Uso
  1. Clonar este repositorio:
     ```bash
     git clone https://github.com/SephbaCode/Filtro-bilateral.git
     
  2. Instalar dependencias necesarias:
     Utilizar el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     
  3. Ejecutar el script principal:
     ```bash
     python src/filtro_bilateral.py
  4. Seleccionar una Imagen para aplicar el filtro (Se puede usar alguna de la carpeta `imagenes prueba`)
  5. Esperar Resultados.
  6. El resultado se vizualizara mediante un plot, en consola se mostraran los tiempos de ejecución.

