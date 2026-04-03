import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, counts=[int(w*100) for w in weights], k=n)
