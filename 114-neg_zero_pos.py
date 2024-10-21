# 114 - Negatives,Zeros and Positives

negative = []
zero = []
positive= []

num = input("Entrez un entier (enter pour quitter): ")

while num != "":
    nb = float(num)

    if nb < 0:
        negative.append(nb)
    elif nb == 0 :
        zero.append(nb)
    else:
        positive.append(nb)
    num = input("Entrez un entier (enter pour quitter): ")

print(negative, zero, positive)
