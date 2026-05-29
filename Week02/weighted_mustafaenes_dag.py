import random

def weighted_srs(data, n, weights, *, with_replacement=False):
    if weights is None: weights = [1] * len(data)
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    w = [int(x * 1000) if x is not None else 1 for x in weights]
    return random.sample(data, k=min(n, len(data)), counts=w)
