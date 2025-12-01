import random

# ERROR 3: Quitamos los corchetes [] para retornar un número entero, no una lista.
def crear_individuo():
    return random.randint(0, 100) # Aumenté el rango a 100 para ver mejor la evolución

def fitness(x):
    return x # Queremos maximizar el número (llegar a 100)
