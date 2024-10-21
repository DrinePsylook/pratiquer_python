# 113 Avoiding Duplicates

word_list = []

word = input("Entrez un mot (enter pour quitter): ")

while word != "":
    if word not in word_list:
        word_list.append(word)
    word = input("Entrez un mot (enter pour quitter): ")

print(word_list)
for wd in word_list:
    print(wd)