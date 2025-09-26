import time
import math

#Datos de Usuarios
Frijolito_Pokemon:3.5
Frijolito_Naruto:5
Frijolito_Demon_Slayer:None

Raichu_Pokemon:2.5
Raichu_Naruto:None
Raichu_Demon_Slayer:3.5

Keny_Pokemon:None
Keny_Naruto:4.5
Keny_Demon_Slayer:4.5

Patas_Pokemon:2.5
Patas_Naruto:3.5
Patas_Demon_Slayer:4.5

#Similitud Frijolito*Raichu
num_Frijolito_Raichu = Frijolito_Pokemon * Raichu_Pokemon
den_Frijolito_Raichu = (math.sqrt(math.pow(Frijolito_Pokemon, 2))) * (math.sqrt(math.pow(Raichu_Pokemon, 2))) 
sim_Frijolito_Raichu = num_Frijolito_Raichu/den_Frijolito_Raichu