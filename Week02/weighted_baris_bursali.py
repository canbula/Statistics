import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, k=n)
    return random.sample(data, n) if weights is None else random.choices(data, weights=weights, k=n)