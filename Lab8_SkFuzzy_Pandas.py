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
