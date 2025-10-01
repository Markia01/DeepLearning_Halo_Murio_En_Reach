import random 
choice = random
import sys 


print(f"random es choice? {random is choice}")

##verificamos carga del modulo
print(f"random en sys.modules:{'random' in sys.modules}")

print(f"ID RANDOM: {id(random)}")
print(f"ID RANDOM: {id(choice)}")