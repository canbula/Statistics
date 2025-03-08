import random 

def weighted_srs(population, n):
    return random.sample(population, n)

population = ["Ali", "Ayşe", "Fatma", "Kazım", "Mehmet", "Ahmet"]

print(weighted_srs(population, 3))
