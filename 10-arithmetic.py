import math
# Arithmetic

a = input("Veuillez entre le premier entier : ")
b = input("Veuillez entre le second entier : ")

try:
    a = int(a) 
    b = int(b)
except ValueError:
    print("Erreur : ce ne sont pas des nombres entiers")

sum = a + b
diff = b - a
product = a * b

if b == 0:
    quotient = "On ne peut pas diviser par 0"
else:
    quotient = a/b

modulo = a % b
log_a = math.log10(a)
res = a+b

print(f"La somme est {sum}. La différence est de {diff}. Le produit est {product}. Le quotient est : {quotient}. Le reste est {modulo}. Le résultat de log10 est {log_a} et le résultat de ab est : {res} ")


