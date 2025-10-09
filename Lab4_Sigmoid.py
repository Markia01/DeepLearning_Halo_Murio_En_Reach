import numpy as np

rand = np.random.seed(42)

W = np.random.rand(4, 4)
b = np.random.rand(4, 1)
X = np.random.rand(4, 1)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
