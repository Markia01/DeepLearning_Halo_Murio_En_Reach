import numpy as np
import time
import random

#* Semilla para reproducibilidad
rng = np.random.default_rng(42) 

#* 3 entradas → 4 salidas
W = rng.random((3, 4))  # Matriz de pesos 3x4
x = np.array([1.0, 0.5, -1.0]) # Vector de entrada (3 valores)

#* Definimos la función de activación sigmoide
def sigmoid(z):
  return 1 / (1 + np.exp(-z))