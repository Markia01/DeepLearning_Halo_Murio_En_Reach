# perceptron used for binary classification for NAND logic gates

input_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

w1, w2, b = -1,-1 , 1.5
def step(x):
    #Función de activación-1
    if x >= 0:
        return 1
    else:
        return 0
    