import random 

def weighted_srs(population, weight, k):
    return random.choices(population, weight, k=k)
