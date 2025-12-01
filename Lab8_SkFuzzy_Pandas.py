import pandas as pd
import numpy as np
import skfuzzy as fuzz
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# --- PASO 1: Carga de Datos (Dataset Personas) ---
# Usamos el diccionario para simular el CSV
data = {
    'edad': [25, 58, 34, 65, 22, 45, 29, 50, 31, 70, 40, 26, 55, 38, 62, 28, 75, 48, 33, 68],
    'salario_anual': [28000, 75000, 45000, 52000, 32000, 68000, 38000, 85000, 
                      42000, 48000, 55000, 31000, 62000, 49000, 51000, 35000, 46000, 72000, 41000, 53000],
    'compra_seguro': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

print("--- Datos Originales ---")
print(df.head())
# --- PASO 2: Lógica Difusa (Ingeniería de Características en la EDAD) ---
# Universo: Edades de 18 a 100 años
x_edad = np.arange(18, 101, 1)

# Definimos las funciones de pertenencia (Triángulos)
# Joven: Alta pertenencia a los 18, baja a los 40
edad_joven = fuzz.trimf(x_edad, [18, 18, 40]) 
# Adulto: Empieza a los 25, pico a los 50, termina a los 75
edad_adulto = fuzz.trimf(x_edad, [25, 50, 75])
# Mayor: Empieza a los 60, pico a los 100
edad_mayor = fuzz.trimf(x_edad, [60, 100, 100])

def obtener_fuzzy_edad(valor, universo):
    # Protegemos contra valores fuera de rango (clipping)
    valor = np.clip(valor, 18, 100)
    g_joven = fuzz.interp_membership(universo, edad_joven, valor)
    g_adulto = fuzz.interp_membership(universo, edad_adulto, valor)
    g_mayor = fuzz.interp_membership(universo, edad_mayor, valor)
    return pd.Series([g_joven, g_adulto, g_mayor])

# Aplicamos la transformación: De 1 columna (edad) sacamos 3 (grados de pertenencia)
df[['f_joven', 'f_adulto', 'f_mayor']] = df['edad'].apply(
    lambda x: obtener_fuzzy_edad(x, x_edad)
)

print("\n--- Feature Engineering (Edad Difusa) ---")
print(df[['edad', 'f_joven', 'f_adulto', 'f_mayor']].head())
