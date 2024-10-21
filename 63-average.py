import sys
# 63 - Average

num = float(input("Entrez un chiffre (0 pour quitter) : "))
n = 0

while num != 0 or num2 != 0 :
    num2 = float(input("Entrez un chiffre  (0 pour quitter) : "))
    n += 1
    num = num + num2
    print(num)
    print(n)
    if num2 == 0: 
        n = n-1
        moyenne = num/n
        print(f"La moyenne de vos {n} chiffres est de {moyenne}")
        sys.exit()
        