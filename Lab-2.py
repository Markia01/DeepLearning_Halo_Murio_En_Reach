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
