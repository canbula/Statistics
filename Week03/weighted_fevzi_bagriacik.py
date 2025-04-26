import random 

def weighted_srs(population, n, weight, with_replacement=False):
    if with_replacement == True or weight != None:
        return random.choices(population, weight=weight, k=n)
    return random.sample(population, n)
