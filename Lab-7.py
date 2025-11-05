# --- 1. IMPORTACIÓN DE BIBLIOTECAS ---

# Importamos la biblioteca TensorFlow y la renombramos con el alias 'tf'.
# *Por qué: La usaremos para crear nuestros datos (linspace)
# y, lo más importante, para acceder a las funciones de activación
import tensorflow as tf

# Importamos el módulo 'pyplot' de la biblioteca 'matplotlib'.
# Le damos el alias 'pl'.
# *Por qué: Pyplot es la interfaz para crear gráficas y visualizaciones en Python.
# Es la herramienta que usaremos para "dibujar" el comportamiento de las funciones.
import matplotlib.pyplot as pl


# --- 2. CREACIÓN DE DATOS DE ENTRADA (EJE X) ---

# Usamos 'tf.linspace' para crear un Tensor (un array de TensorFlow).
# Este tensor se llamará 'x' y contendrá 100 puntos espaciados entre -10.0 y 10.0.
# *Por qué: Este será el "dominio" o eje X de nuestra gráfica.
# Representa el rango de posibles valores de entrada (Z) que
# una neurona podría recibir antes de aplicar su activación.
# a estos datos, es más eficiente crearlos directamente como un Tensor
# de TensorFlow. Si usáramos NumPy, TensorFlow tendría que
# convertir el array de NumPy a un Tensor internamente.
x = tf.linspace(-10.0, 10.0, 100)