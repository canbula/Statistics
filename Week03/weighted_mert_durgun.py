import random

def weighted_srs(data, weights, n, with_replacement=True):
    randomlist = random.choices(data, weights=weights, k=n)
    return randomlist
