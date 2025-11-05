# --- 1. IMPORTACIONES ---

import tensorflow as tf
# Importamos las bibliotecas necesarias.
# Importamos TensorFlow y le damos el alias 'tf'.
# TensorFlow es una biblioteca para computación numérica,
# La usaremos para sus funciones de activación (sigmoid, tanh, relu)

import matplotlib.pyplot as plt
# Importamos el módulo 'pyplot' de la biblioteca 'matplotlib' y le damos el alias 'plt'.
# Matplotlib es la biblioteca estándar en Python para crear gráficas.
# 'pyplot' es una interfaz que facilita la creación de gráficas.

import numpy as np
# Importamos NumPy con el alias 'np'.
# Aunque no lo usamos para cálculos, es crucial para la parte de graficación.
# Matplotlib no entiende el formato 'Tensor' de TensorFlow.
# Usaremos la función .numpy() de TensorFlow para convertir los Tensores
# a 'NumPy arrays', que Matplotlib sí entiende.

print("Bibliotecas importadas correctamente.")