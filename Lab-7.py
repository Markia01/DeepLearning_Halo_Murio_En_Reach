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


