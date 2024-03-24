import random

def weighted_srs(data, n, weights, with_replacement = False):
    sample = []
    if with_replacement:
        return random.choices(population = data, weights = weights, k = n)
    while len(sample) != n:
        sample += random.choices(population = data, weights = weights, k = 1)
        sample = list(set(sample))
    return sample
