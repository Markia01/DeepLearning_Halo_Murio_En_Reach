import time
import math

# Calificaciones de frijolito
Frijolito_Pokemon = 3.5
Frijolito_Naruto = 5
Frijolito_Demon_Slayer = 0

# Calificaciones de raichu
Raichu_Pokemon = 2.5
Raichu_Naruto = 0
Raichu_Demon_Slayer = 3.5

# Calificaciones de kenny
Kenny_Pokemon = 0
Kenny_Naruto = 4.5
Kenny_Demon_Slayer = 4.5

# Calificaciones de patas
Patas_Pokemon = 2.5
Patas_Naruto = 3.5
Patas_Demon_Slayer = 4.5

# Similitud de Frijolito y Raichu
num_Frijolito_Raichu = Frijolito_Pokemon * Raichu_Pokemon
den_Frijolito_Raichu = (math.sqrt(math.pow(Frijolito_Pokemon, 2))
                        ) * (math.sqrt(math.pow(Raichu_Pokemon, 2)))
sim_Frijolito_Raichu = num_Frijolito_Raichu/den_Frijolito_Raichu

# Similitud de Frijolito y Patas
num_Frijolito_Patas = (Frijolito_Pokemon*Patas_Pokemon) + \
    (Frijolito_Naruto*Patas_Naruto)
den_Frijolito_Patas = (math.sqrt(math.pow(Frijolito_Pokemon, 2) + math.pow(Frijolito_Naruto, 2))
                       ) * (math.sqrt(math.pow(Patas_Pokemon, 2) + math.pow(Patas_Naruto, 2)))

sim_Frijolito_Patas = num_Frijolito_Patas/den_Frijolito_Patas

# Predicción de Frijolito y Demon_Slayer
prediction_Frijolito_Demon_Slayer = (sim_Frijolito_Raichu * Raichu_Demon_Slayer +
                                     sim_Frijolito_Patas * Patas_Demon_Slayer) / (sim_Frijolito_Raichu + sim_Frijolito_Patas)

# --- SIMILITUDES CON RAICHU ---

# 1. Similitud de Raichu y Frijolito
num_Raichu_Frijolito = Raichu_Pokemon * Frijolito_Pokemon
den_Raichu_Frijolito = math.sqrt(
    pow(Frijolito_Pokemon, 2)) * math.sqrt(pow(Raichu_Pokemon, 2))
sim_Raichu_Frijolito = num_Raichu_Frijolito/den_Raichu_Frijolito

# 2. Similitud de Raichu y Keny
num_Raichu_Keny = Raichu_Demon_Slayer * Kenny_Demon_Slayer
den_Raichu_Keny = math.sqrt(
    math.pow(Raichu_Demon_Slayer, 2)) * math.sqrt(math.pow(Kenny_Demon_Slayer, 2))
sim_Raichu_Keny = num_Raichu_Keny / den_Raichu_Keny

# 3. Similitud de Raichu y Patas
num_Raichu_Patas = (Raichu_Pokemon * Patas_Pokemon) + \
    (Raichu_Demon_Slayer * Patas_Demon_Slayer)
den_Raichu_Patas = math.sqrt(math.pow(Raichu_Pokemon, 2) + math.pow(Raichu_Demon_Slayer, 2)) * \
    math.sqrt(math.pow(Patas_Pokemon, 2) + math.pow(Patas_Demon_Slayer, 2))
sim_Raichu_Patas = num_Raichu_Patas / den_Raichu_Patas


# --- PREDICCIÓN PARA RAICHU (NARUTO) ---
numerador_raichu = (sim_Raichu_Frijolito * Frijolito_Naruto) + \
    (sim_Raichu_Keny * Kenny_Naruto) + (sim_Raichu_Patas * Patas_Naruto)
denominador_raichu = sim_Raichu_Frijolito + sim_Raichu_Keny + sim_Raichu_Patas
prediction_Raichu_Naruto = numerador_raichu / denominador_raichu

# Similitud para Kenny * Patas
num_Kenny_Patas = (Kenny_Naruto * Patas_Naruto) + \
    (Kenny_Demon_Slayer * Patas_Demon_Slayer)
den_Kenny_Patas = math.sqrt(math.pow(Kenny_Naruto, 2) + math.pow(Kenny_Demon_Slayer, 2)) * \
    math.sqrt(math.pow(Patas_Naruto, 2) + math.pow(Patas_Demon_Slayer, 2))
sim_Kenny_Patas = num_Kenny_Patas / den_Kenny_Patas


# Similitud para Kenny * Raichu
num_Kenny_Raichu = (Kenny_Demon_Slayer * Raichu_Demon_Slayer)
den_Kenny_Raichu = math.sqrt(
    math.pow(Kenny_Demon_Slayer, 2)) * math.sqrt(math.pow(Raichu_Demon_Slayer, 2))
sim_Kenny_Raichu = num_Kenny_Raichu / den_Kenny_Raichu

# Similitud para Kenny * Frijolito
num_Kenny_Frijolito = Kenny_Naruto * Frijolito_Naruto
den_Kenny_Frijolito = math.sqrt(
    math.pow(Kenny_Naruto, 2)) * math.sqrt(math.pow(Frijolito_Naruto, 2))
sim_Kenny_Frijolito = num_Kenny_Frijolito / den_Kenny_Frijolito

# Predicción para Kenny * Pokemon
numerador_kenny = (sim_Kenny_Patas * Patas_Pokemon) + (sim_Kenny_Raichu *
                                                       Raichu_Pokemon) + (sim_Kenny_Frijolito * Frijolito_Pokemon)
denominador_kenny = sim_Kenny_Patas + sim_Kenny_Raichu + sim_Kenny_Frijolito
prediction_Kenny_Pokemon = numerador_kenny / denominador_kenny

print("La prediccion de Kenny para Pokemon es: ",
      round(prediction_Kenny_Pokemon, 2))
print("La prediccion de Raichu para Naruto es: ",
      round(prediction_Raichu_Naruto, 2))
print("La prediccion de Frijolito para Demon Slayer es: ",
      round(prediction_Frijolito_Demon_Slayer, 2))
