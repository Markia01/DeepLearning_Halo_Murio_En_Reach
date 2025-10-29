import tensorflow as tf

# Define a 3x3 input tensor
X = tf.constant([[1.0, 2.0, 3.0],
                 [3.0, 4.0, 5.0], 
                 [5.0, 6.0, 7.0]])

# Define reLu activation
def relu(x):
    return tf.nn.relu(x)

# Define sigmoid activation function
def sigmoid(x):
    return tf.nn.sigmoid(x)

#define hidden layer #1
w1 = tf.Variable(tf.random.normal([3, 3]), name='weight1')
b1 = tf.Variable(tf.random.normal([3]), name='bias1')

#define hidden layer #2
w2= tf.Variable(tf.random.normal([3,3]), name='weight2')
b2= tf.Variable(tf.random.normal([3]), name='bias2')

#define out layer
w_out= tf.Variable(tf.random.normal([3,3]), name='weight out')
b_out= tf.Variable(tf.random.normal([3]), name='bias out')

# --- Cálculos de la Red Neuronal ---

print("Tensor de Entrada (X):")
print(X.numpy())

## 1. Cálculo de la Capa Oculta 1 (con ReLU)
# Usamos tf.matmul para la multiplicación de matrices (Entrada * Pesos) + Sesgo
z1 = tf.matmul(X, w1) + b1
# Aplicamos la activación ReLU
h1 = relu(z1)

print("\n--- Activación Capa Oculta 1 (ReLU) ---")
print(h1.numpy())

## 2. Cálculo de la Capa Oculta 2 (con Sigmoide)
# La entrada a esta capa es la salida de la capa anterior (h1)
z2 = tf.matmul(h1, w2) + b2
# Aplicamos la activación Sigmoide
h2 = sigmoid(z2)