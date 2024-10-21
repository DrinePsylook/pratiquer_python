# 66 - No more penny

pennies_per_nickel = 5
nickel = 0.05

# Même s’il est très improbable que le nombre de pièces d’un nickel change un jour, il est possible (même probable) que nous devions mettre à jour notre programme à un moment donné dans le futur, qu'il arrondit au centime le plus proche. L'utilisation de constantes facilitera l'exécution de cette mise à jour quand cela est nécessaire.

# total = 0.00

# line = input("Entrez le prix de notre objet (blanc pour quitter): ")

# while line != "":
#     total = total + float(line)
#     line = input("Entrez le prix de notre objet (blanc pour quitter): ")
#     print("Le montant à payer exact est : %.02f" % total)
#     rounding_indicator = total * 100 % pennies_per_nickel
#     if rounding_indicator < pennies_per_nickel / 2:
#         cash_total = total - rounding_indicator / 100
#     else:
#         cash_total = total + nickel - rounding_indicator / 100
#         print("Le montant en liquide à payer est : %.02f" % cash_total)