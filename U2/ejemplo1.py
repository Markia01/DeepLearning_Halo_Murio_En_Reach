import time 

import math

#!Funcionamiento de la compuerta AND

#?Valores "A" y "B" de compuerta AND

entrada1=[[0,0],[0,1],[1,0],[1,1]]

#?Pesos
w1=1
w2=5.5

def stepFunction(suma):
    #//FUNCION DE ACTIVACION
    if suma>=1:
        return 1
    else:
        return 0
    
##SIMULACION DE LA RED NEURONAL

print("Simulacion de la compuerta AND")

for x in entrada:
    x1,x2=x


#!Calculo de la salida de neurona

z=x1*w1+x2*w2+1 #1 Sera la bias más adelante

salida = stepFunction(z)

print(f"Etrada : {x} -> z={z:.1f}, salida={salida}")

#time.sleep(1)