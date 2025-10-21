import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configuración Inicial ---
# * Semilla para reproducibilidad
rng = np.random.default_rng(42)  # random number generator

# * 3 entradas → 4 salidas
W = rng.random((3, 4))  # Matriz de pesos 3x4    W = [weights]
X = np.array([1.0, 0.5, -1.0])  # Vector de entrada (3 valores)
