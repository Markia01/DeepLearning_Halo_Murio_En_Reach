# Import the necessary libraries
import numpy as np
import time
import random

# Seed for reproducibility, so we get the same "random" numbers every time
rng = np.random.default_rng(42)

# Define the network architecture: 3 inputs connected to 4 outputs
W = rng.random((3, 4))      # Create a 3x4 Weight matrix
x = np.array([1.0, 0.5, -1.0])  # Create an input vector with 3 values

# Define the ReLU (Rectified Linear Unit) activation function
# It returns 0 for any negative input, or the input itself if it's 0 or positive.


def relu(z):
    return np.maximum(0, z)

# --- Feedforward Process ---


# 1. Calculate the linear output (dot product of input * weights)
linear_output = x @ W  # The '@' symbol is shorthand for np.dot(x, W)

# 2. Apply the ReLU activation function to the linear output
activated_output = relu(linear_output)

# --- Display Results ---

# Print the initial weights and input
print("Weight Matrix (3x4):")
print(W)
print("\nInput Vector:")
print(x)

# Print the outputs at each stage
print("\nLinear Output (before ReLU):")
print(linear_output)
print("\nActivated Output (after ReLU):")
print(activated_output)
