import numpy as np
import skfuzzy as fuzz

#Definimos el rango del unoverso (temperaturas de 0 a 30 grados)
x_temp = np.arange(0, 31, 1)

#2. Definimos la función de pertenencia triangular
# trimf (X, [inicio, centro, fin])

mu_frio = fuzz.trimf(x_temp, [0, 0, 20])

# Evaluamos la pertenencia de algunos valores
valores=[0, 5, 10, 15, 20]
for valor in valores:
    pertenencia = fuzz.interp_membership(x_temp, mu_frio, valor)
    print(f"Temperatura: {valor} °C μ_frio: ({valor})={pertenencia:.2f}")