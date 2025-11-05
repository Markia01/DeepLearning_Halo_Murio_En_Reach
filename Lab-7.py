# --- 1. IMPORTACIÓN DE BIBLIOTECAS ---

# Importamos la biblioteca TensorFlow y la renombramos con el alias 'tf'.
# *Por qué: La usaremos para crear nuestros datos (linspace)
# y, lo más importante, para acceder a las funciones de activación
import tensorflow as tf

# Importamos el módulo 'pyplot' de la biblioteca 'matplotlib'.
# Le damos el alias 'pl'.
# *Por qué: Pyplot es la interfaz para crear gráficas y visualizaciones en Python.
# Es la herramienta que usaremos para "dibujar" el comportamiento de las funciones.
import matplotlib.pyplot as pl


# --- 2. CREACIÓN DE DATOS DE ENTRADA (EJE X) ---

# Usamos 'tf.linspace' para crear un Tensor (un array de TensorFlow).
# Este tensor se llamará 'x' y contendrá 100 puntos espaciados entre -10.0 y 10.0.
# *Por qué: Este será el "dominio" o eje X de nuestra gráfica.
# Representa el rango de posibles valores de entrada (Z) que
# una neurona podría recibir antes de aplicar su activación.
# a estos datos, es más eficiente crearlos directamente como un Tensor
# de TensorFlow. Si usáramos NumPy, TensorFlow tendría que
# convertir el array de NumPy a un Tensor internamente.
x = tf.linspace(-10.0, 10.0, 100)

# --- 3. APLICACIÓN DE FUNCIONES DE ACTIVACIÓN (EJE Y) ---

# Aplicamos la función Sigmoid a cada uno de los 100 puntos en 'x'.
# 'tf.nn.sigmoid' comprime cualquier número real (de -inf a +inf)
# y lo mapea a un rango estrictamente entre 0 y 1.
# *Por qué: Usamos la función de 'tf.nn' porque está optimizada
# y es "numéricamente estable" (evita errores con números muy
# grandes o muy pequeños).
# *Alternativa: Podríamos escribir la fórmula matemática:
# 1.0 / (1.0 + tf.exp(-x)). Esto no se recomienda porque puede
# causar problemas de precisión o desbordamiento (overflow)
# si 'x' es muy grande.
y_sigmoid = tf.nn.sigmoid(x)

# Aplicamos la función Tanh (Tangente Hiperbólica) a 'x'.
# Es similar a Sigmoid, pero comprime los valores a un
# rango entre -1 y 1.
# *Por qué: Al estar "centrada en cero", a menudo ayuda a que
# las redes neuronales converjan (aprendan) más rápido que Sigmoid.
y_tanh = tf.nn.tanh(x)

# Aplicamos la función ReLU (Rectified Linear Unit) a 'x'.
# Esta es la función de activación más popular en deep learning.
# Su regla es simple: si x > 0, la salida es x. Si x <= 0, la salida es 0.
# *Por qué: Es computacionalmente muy rápida (sin exponenciales)
# y ayuda a mitigar el problema del "desvanecimiento del gradiente".
# *Alternativa: Podríamos escribirla como 'tf.maximum(0, x)',
# que tendría exactamente el mismo resultado. 'tf.nn.relu'
# es simplemente el nombre estándar de la industria.
y_relu = tf.nn.relu(x)
