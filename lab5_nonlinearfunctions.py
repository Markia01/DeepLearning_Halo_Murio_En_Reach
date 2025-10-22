import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configuración Inicial ---
# * Semilla para reproducibilidad
rng = np.random.default_rng(42)  # random generador de numeros aleatorios

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
# Es posible cambiar esta variable por: 'tanh', 'sigmoid', 'relu', 'linear'
activation_choice = 'tanh'

match activation_choice:
    case 'tanh':
        y_activada = np.tanh(y_lineal)
        # Define la curva para la gráfica
        x_curve = np.linspace(-5, 5, 100)
        y_curve = np.tanh(x_curve)
        title = "Función Tangente Hiperbólica (tanh) y Salidas"
        y_label = "tanh(X)"

    case 'sigmoid':
        y_activada = sigmoid(y_lineal)
        # Define la curva para la gráfica
        x_curve = np.linspace(-8, 8, 100)
        y_curve = sigmoid(x_curve)
        title = "Función Sigmoide y Salidas"
        y_label = "sigmoid(X)"

    case 'relu':
        y_activada = np.maximum(0, y_lineal)
        # Define la curva para la gráfica
        x_curve = np.linspace(-5, 5, 100)
        y_curve = np.maximum(0, x_curve)
        title = "Función ReLU (Rectified Linear Unit) y Salidas"
        y_label = "ReLU(X)"

    case 'linear' | _:  # Caso 'linear' o cualquier otro valor (default)
        y_activada = y_lineal
        # Define la curva para la gráfica (identidad)
        x_curve = np.linspace(-5, 5, 100)
        y_curve = x_curve
        title = "Función Lineal (Identidad) y Salidas"
        y_label = "X"

# --- 4. Visualización ---
# Gráfica de la función de activación elegida
plt.plot(x_curve, y_curve, label=f"Curva {activation_choice}(x)")

# Graficar las salidas activadas como líneas horizontales
for i, val in enumerate(y_activada):
    plt.hlines(val, x_curve[0], x_curve[-1], colors='r', linestyles='--',
               label=f'Output {i+1}: {val:.2f}' if i == 0 else None)

