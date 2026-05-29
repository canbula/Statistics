import random

def weighted_srs(data, n, weights, with_replacement=False):
    return random.choices(data, weights=weights, k=n)
