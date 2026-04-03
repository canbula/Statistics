import random

def weighted_srs(data, n, weights, *, with_replacement=False):
    w = None if with_replacement else weights
    return random.choices(data, weights=w, k=n)
