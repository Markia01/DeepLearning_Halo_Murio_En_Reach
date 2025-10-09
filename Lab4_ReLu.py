#Importing the libraries
import numpy as np
import time 
import random

#* Seed for reproducibility
rng = np.random.default_rng(42)

#* 3 inputs → 4 outputs
W = rng.random((3, 4)) # 3x4 Weight matrix
x = np.array([1.0, 0.5, -1.0]) # Input vector (3 values)

#* Inicio del Feedforward (producto punto entrada * pesos)
y = x @ W  # Equivalente a np.dot(x, W)
#*np.dot()

#Inicio de funcion de activacion ReLu
def relu(z):
    return np.maximum(0,z) #se aplica el max a cada elemento

#salida de ReLu
    y_relu = relu(y)
#* Mostrar resultados
print("Matriz de pesos (3x4):")
print(W)
print("\nEntrada:")
print(x)
print("\nSalida:")
print(y) 
