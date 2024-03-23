import random

def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement:
        randomlist = random.choices(data, k=n, weights=weights)
    else:
        randomlist = random.sample(data, n)
    return randomlist
