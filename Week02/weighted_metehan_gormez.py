import random

def weighted_srs(data, n, weights=None, with_replacement=False):
    if weights is None:
        if with_replacement:
            return random.choices(data, k=n)
        else:
            return random.sample(data, n)
    else:
        if with_replacement:
            return random.choices(data, weights=weights, k=n)
        else: 
            return random.choices(data, weights=weights, k=n)
