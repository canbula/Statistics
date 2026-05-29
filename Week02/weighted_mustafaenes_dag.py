import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.sample(data, counts=None, k=n) if weights is None else \
               [val for val, weight in zip(data, weights) if weight > 0]
        return random.sample(data, k=n, counts=weights)
