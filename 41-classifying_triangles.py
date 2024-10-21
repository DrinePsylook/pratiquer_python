# 41 - Classifying Triangles

first_side = float(input('Taille de votre premier côté : '))
second_side = float(input('Taille de votre second côté : '))
third_side = float(input('Taille de votre troisième côté : '))

if first_side == second_side and second_side == third_side:
    print("c'est un triangle équilatéral")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("c'est un triangle isocèle")
else :
    print("c'est un triangle scalène")