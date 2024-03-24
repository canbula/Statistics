import random

def weighted_srs(data, n, weights, with_replacement = False):
    if with_replacement:
        return random.choices(population = data, weights = weights, k = n)
    return random.sample(data, min(n, len(data)))
