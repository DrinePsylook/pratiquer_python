# Sum of the first n Positive integers

start = input('Combien de chiffres voulez-vous entrer ? ')
n = int(start)
x = 0


for i in range(n):
    entier_positif = float(input("Veuillez entrer un entier positif : "))
    if entier_positif < 0:
        print("Ce n'est pas un nombre entier")
    else: 
        x = x + entier_positif

print(f"La somme des nombres saisis est de {x}")
    
    

