import random

def weighted_srs(data, n, weights, with_replacement= True):
    return random.choices(data, weights=weights, k=n) if with_replacement else random.sample(data, n)
