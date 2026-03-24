import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights:
        res = random.choices(data, weights=weights, k=n)
        return res if with_replacement else list(dict.fromkeys(res))[:n]
    return random.sample(data, n)
