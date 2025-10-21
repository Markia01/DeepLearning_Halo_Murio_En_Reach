import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configuración Inicial ---
# * Semilla para reproducibilidad
rng = np.random.default_rng(42)  # random number generator

# * 3 entradas → 4 salidas
W = rng.random((3, 4))  # Matriz de pesos 3x4    W = [weights]
X = np.array([1.0, 0.5, -1.0])  # Vector de entrada (3 valores)

# * Definición de funciones de activación
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# --- 2. Cálculo Lineal ---
# Producto punto (Suma ponderada)
weighted_sum = X @ W
y_lineal = weighted_sum  # Salida antes de activar

# --- 3. REQUISITO: Sentencia Match-Case para Activación ---
# Puedes cambiar esta variable a: 'tanh', 'sigmoid', 'relu', 'linear'
activation_choice = 'tanh'
