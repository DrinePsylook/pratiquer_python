# 13 - Making Change

cents = int(input("Entrez le numéro de cents : "))

cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

print(cents // cents_per_toonie, " toonies")
cents = cents % cents_per_toonie

print(cents // cents_per_loonie, " loonies")
cents = cents % cents_per_loonie

print(cents // cents_per_quarter, " quarters")
cents = cents % cents_per_quarter

print(cents // cents_per_dime, " dimes")
cents = cents % cents_per_dime

print(cents // cents_per_nickel, " nickels")
cents = cents % cents_per_nickel

print(" ", cents, "pennies")