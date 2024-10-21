# 36 - Dog Years

dog_age = float(input("Quel âge à votre chien (en année) ? "))

if dog_age < 0 :
    print("Erreur : les nombres négatifs ne peuvent pas être convertis")
elif dog_age <= 2 :
    conversion = dog_age*10.5
    print(f"Votre chien a {conversion} années humaines.")
else:
    conversion = dog_age*4
    print(f"Votre chien a {conversion} années humaines.")


