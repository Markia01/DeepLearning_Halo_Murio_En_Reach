import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

print(f"TensorFlow Version: {tf.__version__}")

# - 1. Definiciones de Funciones -


def relu(x):
    """Aplica la activación Rectified Linear Unit (ReLU)."""
    return tf.nn.relu(x)


def sigmoid(x):
    """Aplica la activación Sigmoid."""
    return tf.nn.sigmoid(x)


def tanh(x):
    """Aplica la activación Tangente Hiperbólica (Tanh)."""
    # Esta es la tercera función que pedía la imagen.
    return tf.nn.tanh(x)

# - 2. Definición de la Red Neuronal (Arquitectura 2-3-3)


# Entradas (Inputs)
X = tf.constant([
    [1.0, 2.0],
    [0.5, -1.0],
    [-2.0, 1.5],
    [0.0, -0.5]
], dtype=tf.float32)

# Capa Oculta (1 capa con 3 neuronas)
w1 = tf.Variable(tf.random.normal([2, 3]), name='weight1')
b1 = tf.Variable(tf.random.normal([3]), name='bias1')


# 2.3. Capa de Salida (3 salidas)
# Necesitamos mapear [3 neuronas] -> [3 salidas]
# w_out (pesos) debe tener forma [3, 3]
# b_out (bias) debe tener forma [3]
w_out = tf.Variable(tf.random.normal([3, 3]), name='weight_out')
b_out = tf.Variable(tf.random.normal([3]), name='bias_out')


# --- 3. Cálculos de la Red y Observación de Activaciones ---

print("--- 3.1. Cálculos de la Red ---")
print("Input Tensor (X):")
print(X.numpy())
print("Shape:", X.shape)

# 3.2. Cálculo de la Capa Oculta (ANTES de activar)
# Esta es la "combinación lineal": (X * w1) + b1
# z1 tendrá los valores 'en bruto' para las 3 neuronas.
z1 = tf.matmul(X, w1) + b1

print("\nCapa Oculta (Pre-Activación, z1):")
print(z1.numpy())
print("Shape:", z1.shape)

# 3.3. OBSERVACIÓN DE ACTIVACIONES (Como pide la imagen)
# Ahora aplicamos las 3 funciones a 'z1' para ver qué haría cada una.
h_relu = relu(z1)
h_sigmoid = sigmoid(z1)
h_tanh = tanh(z1)

print("\n--- 3.2. Observación de Funciones de Activación ---")
print("\nResultado si usamos ReLU (h_relu):")
print(h_relu.numpy())

print("\nResultado si usamos Sigmoid (h_sigmoid):")
print(h_sigmoid.numpy())

print("\nResultado si usamos Tanh (h_tanh):")
print(h_tanh.numpy())

# 3.4. Cálculo de la Salida Final
# Para completar la red, elegiremos UNA activación.
# Usaremos h_relu (la más común) para alimentar la capa de salida.
z_out = tf.matmul(h_relu, w_out) + b_out
# y_final es la salida de la red (sin activación final)
y_final = z_out

print("\n--- 3.3. Salida Final de la Red (usando ReLU) ---")
print(y_final.numpy())
print("Output shape:", y_final.shape)


# --- 4. Parte Gráfica (Requerimiento de la Imagen) ---
# Para "observar el comportamiento", graficamos las funciones
# en un rango amplio, no solo con los datos de la red.

print("\n--- 4. Generando Gráfica de Comportamiento ---")

# 4.1. Creamos un rango de entrada de -10 a 10
x_graph = tf.linspace(-10.0, 10.0, 100)

# 4.2. Aplicamos las funciones a ese rango
y_sigmoid_graph = sigmoid(x_graph)
y_tanh_graph = tanh(x_graph)
y_relu_graph = relu(x_graph)

# 4.3. Creamos la gráfica con Matplotlib
plt.figure(figsize=(10, 7))
plt.plot(x_graph.numpy(), y_sigmoid_graph.numpy(), label='Sigmoid', color='blue')
plt.plot(x_graph.numpy(), y_tanh_graph.numpy(), label='Tanh', color='green')
plt.plot(x_graph.numpy(), y_relu_graph.numpy(), label='ReLU', color='red')

# 4.4. Configuramos la gráfica
plt.title('Comportamiento de Funciones de Activación')
plt.xlabel('Valores de Entrada (z)')
plt.ylabel('Valores de Salida (Activación)')
plt.legend()
plt.grid(True)
plt.ylim(-1.5, 2.0) # Ajuste para ver bien las 3 funciones
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# 4.5. Mostramos la gráfica
plt.show()