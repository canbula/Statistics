import random 

def weighted_srs(population, weight, k):
    ##population = ["Ali", "Ayşe", "Fatma", "Kazım", "Mehmet"]
    ##weight = [20, 20, 20, 20, 20]
    ##k = 3
    return random.choices(population, weight, k=k)

print(weighted_srs(["Ali", "Ayse", "Fatma", "Kazım", "Mehmet"], [20, 20, 20, 20, 20], 3))
