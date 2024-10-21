# 110 - Sorted Order

data = []

num = int(input("Entrez un nombre (0 pour sortir) : "))

while num != 0:
    data.append(num)
    num = int(input("Entrez un nombre (0 pour sortir) : "))

data.sort()

for num in data:
    print(num)