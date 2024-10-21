import sys

# 69 - Admission Cost

age = input('Voulez-vous acheter des billets (O/N) : ').upper()

cpt = 0
somme = 0

if age == "O":
    while age != 0:
        age = int(input("Veuillez renseigner l'âge du visiteur (0 pour quitter): "))
        if age <= 2 :
            ticket_price = 0
        elif age <= 12:
            ticket_price = 14
        elif age < 65:
            ticket_price = 23
        else :
            ticket_price = 18

        somme = somme + ticket_price
        cpt += 1
        if age == 0:
            cpt = cpt-1
            print(f"le prix total des {cpt} billets d'entrée est de {somme}")
else :
    sys.exit()