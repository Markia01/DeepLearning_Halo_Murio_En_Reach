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

# --- Layer Definitions ---

# define hidden layer #1 (Input: 3, Output: 3)
w1 = tf.Variable(tf.random.normal([3, 3]), name='weight1')
b1 = tf.Variable(tf.random.normal([3]), name='bias1')

# define hidden layer #2 (Input: 3, Output: 3)
w2 = tf.Variable(tf.random.normal([3, 3]), name='weight2')
b2 = tf.Variable(tf.random.normal([3]), name='bias2')
    
# define out layer (Input: 3, Output: 2)
w_out = tf.Variable(tf.random.normal([3, 2]), name='weight_out')
b_out = tf.Variable(tf.random.normal([2]), name='bias_out')


# --- Neural Network Calculations ---

print("Input Tensor (X):")
print(X.numpy())
print("Shape:", X.shape)

## 1. Hidden Layer 1 (with ReLU)
# (Input: 3, Output: 3)
z1 = tf.matmul(X, w1) + b1
h1 = relu(z1)

print("\n--- Hidden Layer 1 Activation (ReLU) ---")
print(h1.numpy())
print("Shape:", h1.shape)


## 2. Hidden Layer 2 (with Sigmoid)
# (Input: 3, Output: 3)
z2 = tf.matmul(h1, w2) + b2
h2 = sigmoid(z2)

print("\n--- Hidden Layer 2 Activation (Sigmoid) ---")
print(h2.numpy())
print("Shape:", h2.shape)


## 3. Output Layer (No activation in this example)
# (Input: 3, Output: 2)
z_out = tf.matmul(h2, w_out) + b_out
# 'y_final' is now the final output
y_final = z_out.numpy() 


print("\n--- Neural Network Output (3 samples, 2 outputs each) ---")
print(y_final)
print("Output shape:", y_final.shape)
