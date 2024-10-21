def pythatgore(width, height):
    c = width ** 2 + height ** 2
    return c

side1 = float(input("Longueur du premier côté : "))
side2 = float(input("Longueur du deuxième côté : "))

result = pythatgore(side1, side2)
print(result)