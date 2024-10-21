import sys
# 11 - Fuel Efficiency

MPG = float(input("Veuillez saisir votre consommation d'essence (en miles par galon) : "))

try: 
    MPG
except ValueError:
    print("Erreur : ce n'est pas un nombre")
    sys.exit()

l100km = (2.352/MPG)*100

print(f"Le rendement énergétique équivalent au {MPG} miles par galon est de {l100km} litres par 100 km")