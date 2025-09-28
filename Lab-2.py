import time
import math

# Datos de Usuarios
Frijolito_Pokemon: 3.5
Frijolito_Naruto: 5
Frijolito_Demon_Slayer: None

Raichu_Pokemon: 2.5
Raichu_Naruto: None
Raichu_Demon_Slayer: 3.5

Keny_Pokemon: None
Kenny_Naruto: 4.5
Kenny_Demon_Slayer: 4.5

Patas_Pokemon: 2.5
Patas_Naruto: 3.5
Patas_Demon_Slayer: 4.5

# Similitud Frijolito*Raichu
num_Frijolito_Raichu = Frijolito_Pokemon * Raichu_Pokemon
den_Frijolito_Raichu = (math.sqrt(math.pow(Frijolito_Pokemon, 2))
                        ) * (math.sqrt(math.pow(Raichu_Pokemon, 2)))
sim_Frijolito_Raichu = num_Frijolito_Raichu/den_Frijolito_Raichu

# Similitud Frijolito*Patas
num_Frijolito_Patas = (Frijolito_Pokemon*Patas_Pokemon) + \
    (Frijolito_Naruto*Patas_Naruto)
den_Frijolito_Patas = (math.sqrt(math.pow(Frijolito_Pokemon, 2) + math.pow(Frijolito_Naruto, 2))
                       ) * (math.sqrt(math.pow(Patas_Pokemon, 2) + math.pow(Patas_Naruto, 2)))

sim_Frijolito_Patas = num_Frijolito_Patas/den_Frijolito_Patas

# Predicción Frijolito*Demon_Slayer
prediction_Frijolito_Demon_Slayer = (sim_Frijolito_Raichu * Raichu_Demon_Slayer +
                                     sim_Frijolito_Patas * Patas_Demon_Slayer) / (sim_Frijolito_Raichu + sim_Frijolito_Patas)

# --- SIMILITUDES CON RAICHU ---

# 1. Similitud Raichu * Frijolito
#Es la misma que ya calculamos, la similitud es mutua.
num_Raichu_Frijolito = Raichu_Pokemon * Frijolito_Pokemon
den_Raichu_Frijolito = math.sqrt(pow (Frijolito_Pokemon,2)) * math.sqrt(pow(Raichu_Pokemon, 2))
sim_Raichu_Frijolito = num_Raichu_Frijolito/den_Raichu_Frijolito

# 2. Similitud Raichu * Keny
num_Raichu_Keny = Raichu_Demon_Slayer * Kenny_Demon_Slayer
den_Raichu_Keny = math.sqrt(math.pow(Raichu_Demon_Slayer, 2)) * math.sqrt(math.pow(Kenny_Demon_Slayer, 2))
sim_Raichu_Keny = num_Raichu_Keny / den_Raichu_Keny

# 3. Similitud Raichu * Patas
num_Raichu_Patas = (Raichu_Pokemon * Patas_Pokemon) + (Raichu_Demon_Slayer * Patas_Demon_Slayer)
den_Raichu_Patas = math.sqrt(math.pow(Raichu_Pokemon, 2) + math.pow(Raichu_Demon_Slayer, 2)) * math.sqrt(math.pow(Patas_Pokemon, 2) + math.pow(Patas_Demon_Slayer, 2))
sim_Raichu_Patas = num_Raichu_Patas / den_Raichu_Patas


# --- PREDICCIÓN PARA RAICHU (NARUTO) ---

# Usamos las calificaciones de Naruto de Frijolito, Keny y Patas
numerador_raichu = (sim_Raichu_Frijolito * Frijolito_Naruto) + (sim_Raichu_Keny * Kenny_Naruto) + (sim_Raichu_Patas * Patas_Naruto)
denominador_raichu = sim_Raichu_Frijolito + sim_Raichu_Keny + sim_Raichu_Patas
prediction_Raichu_Naruto = numerador_raichu / denominador_raichu