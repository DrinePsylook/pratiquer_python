import sys
# Area of a field

width = input("Quelle est la largeur du champ ? (en mètre) ")
length = input("Quelle est la longueur du champ  ? (en mètre) ")

try:
    width = float(width) 
    length = float(length)
except ValueError:
    print("Erreur : ceci n'est pas un nombre")
    sys.exit()

# print(type(width))
# print(type(length))

width_feet = width *3.28
length_feet = length* 3.28

area_feet = width_feet * length_feet
nb_square_feet = area_feet/43560

print(f"Il y a {nb_square_feet} acres dans ce champ")