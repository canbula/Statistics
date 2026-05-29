import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    res = list(dict.fromkeys(random.choices(data, weights=weights, k=n*10)))
    return res[:n]
