##Neurona con ReLu
#Implementacion de las librerias
import numpy as np
import time 
import random

#* Semilla para reproducibilidad
rng = np.random.default_rng(42)  
 
#* 3 entradas → 4 salidas
W = rng.random((3, 4))   # Matriz de pesos 3x4
x = np.array([1.0, 0.5, -1.0])  # Vector de entrada (3 valores)


#* Feedforward (producto punto entrada * pesos)
y = x @ W  # Equivalente a np.dot(x, W)
#*np.dot()

#Funcion de activacion ReLu
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
