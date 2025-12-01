import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

data= pd.read_csv('personas.csv')
print("Data originales  :\n")

max_edad = np.max(data['Edad'])
data["Edad_Normalizada"] = data['Edad']/max_edad

print("Data normalizada :\n")
print(data.head())

plt.plot(data["Nombre"], data['Edad'], label="Edad real", marker="o")
plt.plot(data["Nombre"], data['Edad_Normalizada'] * max_edad, label="Edad normalizada * max", marker="x")
plt.title("Comparación entre Edad real y normalizada")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.legend()
plt.grid(True)
plt.show()