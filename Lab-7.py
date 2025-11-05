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