def fare(distance, fare_sup):
    base_fare = 4.00
    nb_dist = distance / 140
    fare_total = fare_sup * nb_dist + base_fare
    return fare_total

total = fare(10000, 0.25)
print(total)
