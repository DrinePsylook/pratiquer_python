import numpy as np
# 88 - Median of Three Values

def calculate_median(num1, num2, num3):
    my_number = [num1, num2, num3]
    number_asc = np.sort(my_number)
    nb_median = (3 + 1) / 2
    median = number_asc[int(nb_median) - 1]
    return median

nb1 = float(input("Premier nombre : "))
nb2 = float(input("Deuxième nombre : "))
nb3 = float(input("Troisième nombre : "))


median = calculate_median(nb1,nb2,nb3)
print(median)