def shipping(number_items):
    rate1 = 10.95
    other_rate = 2.95
    nb_subsequent_item = number_items - 1
    total = rate1 + (other_rate * nb_subsequent_item)
    return total

nb_items = int(input("Combien d'articles dans le panier : "))

total = shipping(nb_items)
print(total)