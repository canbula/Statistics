import random

def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement: return random.choices(data, k=n)
    if weights is None: return random.sample(data, k=n)
    return random.choices(data, weights=weights, k=n)
