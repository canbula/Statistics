import random

def weighted_srs(data, n, weights, with_replacement=False):
    if weights is None:
        if with_replacement:
            return random.choices(data, k=n)
        return random.sample(data, n)
    return random.choices(data, weights=weights, k=n)
