import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement == True or weights != None:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, n)
