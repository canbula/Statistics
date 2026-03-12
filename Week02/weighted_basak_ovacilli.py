import random

def weighted_srs(data, n, weights, with_replacement=False):
    if weights is not None or with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, n)
