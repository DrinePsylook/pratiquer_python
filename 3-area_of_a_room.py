# 3 - Area of a room

width = float(input("Quelle est la largeur de la pièce ? (en mètre) "))
length = input("Quelle est la longueur de la pièce ? (en mètre) ")

# print(type(width))
# print(type(length))

try:
    area = width * length
    print(f"la pièce mesure {area} m²")
except ValueError:
    print("Erreur : ceci n'est pas un nombre")

