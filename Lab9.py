import random

# ERROR 3: Quitamos los corchetes [] para retornar un número entero, no una lista.


def crear_individuo():
    # Aumenté el rango a 100 para ver mejor la evolución
    return random.randint(0, 100)


def fitness(x):
    return x  # Queremos maximizar el número (llegar a 100)

def seleccion(poblacion):
    # Torneo simple: escogemos 2 al azar y gana el mayor
    a = random.choice(poblacion)
    b = random.choice(poblacion)
    return a if fitness(a) > fitness(b) else b


def cruzar(p1, p2):
    # Ahora sí podemos sumar y dividir porque son números
    return int((p1 + p2) / 2)


def mutar(x):
    # Probabilidad de mutación del 10%
    if random.random() < 0.1:
        return x + random.randint(-5, 5)  # Pequeña variación
    return x

