import random

def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    w = [1] * len(data) if weights is None else weights
    return random.sample(data, k=n, counts=[int(x * 1000) for x in w])
