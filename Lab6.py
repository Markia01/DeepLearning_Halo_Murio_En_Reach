import tensorflow as tf

# Define a 3x3 input tensor
X = tf.constant([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [5.0, 6.0, 7.0]])

# Define reLu activation
def relu(x):
    return tf.nn.relu(x)

# Define sigmoid activation function
def sigmoid(x):
    return tf.nn.sigmoid(x)

w1 = tf.Variable(tf.random.normal([3, 2]), name='weight1')
b1 = tf.Variable(tf.random.normal([2]), name='bias1')
