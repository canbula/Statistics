import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement is True or weights is not None:
        sample = random.choices(population = data, k = n, weights = weights)
    else:
        sample = random.sample(population = data, k = n)
    return sample
