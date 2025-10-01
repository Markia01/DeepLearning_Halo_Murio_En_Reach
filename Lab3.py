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
    
print("Simulación de una sola neurona (NAND lógico):\n")

for x in input_data: #for para tomar los valores del imput data y asignarlos a x1 y x2)
    x1, x2 = x
    # cálculo de la neurona, (a los valores de x se les multiplica los pesos respectivos 
    # y al final se suma el bias)
    z = x1*w1 + x2*w2 + b
