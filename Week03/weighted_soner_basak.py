import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights is not None:
        randomlist = random.choices(data, r=n, weights=weights)
    else:
        randomlist = random.sample(data, n)
    return randomlist
