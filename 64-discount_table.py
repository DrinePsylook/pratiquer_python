# 64 - Discount Table

articles = [4.95, 9.95, 14.95, 19.95, 24.95]

original_price = 0
percent = 60/100
new_price = 0
reduction = 0

for article in articles:
    original_price = article
    new_price = original_price*percent
    reduction = original_price - new_price
    print(f" Prix original : {format(original_price, '.2f')}")
    print(f" Réduction : {format(reduction, '.2f')}")
    print(f"Nouveau prix: {format(new_price, '.2f')}")
    print("\n")