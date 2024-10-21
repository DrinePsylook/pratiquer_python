import sys
# 5 - Bottle deposits

little_bottle = input("Combien de bouteilles de 1 litre ou moins : ")
big_bottle = input("Combien de bouteilles de plus de 1 litre : ")
little_caution = 0.10
big_caution = 0.25

try:
    little_bottle = int(little_bottle) 
    big_bottle = int(big_bottle)
except ValueError:
    print("Erreur : ceci n'est pas un nombre entier")
    sys.exit()

tarif_total = (little_bottle * little_caution) + (big_bottle * big_caution)

print(f"Votre remboursement est de : {format(tarif_total, '.2f')} $")