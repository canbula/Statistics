import random

def weighted_srs(data, n, weights, with_replacement = False):
    if with_replacement or weights is not None:
        return random.choices(data, k = n, weights = weights)
    else:
        return random.sample(data, n)
