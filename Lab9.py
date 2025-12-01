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

def ga():
    # Creamos 5 individuos iniciales
    poblacion = [crear_individuo() for _ in range(5)]

    print(f"Población Inicial: {poblacion}")

    for gen in range(10): # Haremos 10 generaciones
        nueva = []
        for _ in range(len(poblacion)):
            p1 = seleccion(poblacion)
            p2 = seleccion(poblacion)
            hijo = cruzar(p1, p2)
            nueva.append(mutar(hijo))
        
        poblacion = nueva
        # ERROR 2 ARREGLADO: El return estaba aquí, cortando el ciclo.
        # Lo hemos quitado para que el bucle termine sus 10 vueltas.
        print(f"Generación {gen+1}: {poblacion}")
    
    # Al final del proceso, buscamos al mejor
    mejor = max(poblacion, key=fitness)
    print(f"\n--- Resultado Final ---")
    print(f"Mejor solución encontrada: {mejor}")
    return poblacion

# ERROR 1 ARREGLADO: Llamamos a la función para que el código corra
if _name_ == "_main_":
    ga()