import random

def weighted_srs(data, n, weights=None, *, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, k=n, counts=None if not weights else [int(w*100) for w in weights])
