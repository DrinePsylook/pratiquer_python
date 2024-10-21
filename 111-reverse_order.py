# 110 - Reverse order

data = []

num = int(input("Entrez un nombre (0 pour sortir) : "))

while num != 0:
    data.append(num)
    num = int(input("Entrez un nombre (0 pour sortir) : "))

data.reverse()

for num in data:
    print(num)