import random

def weighted_srs(data, weights, n):
    randomlist = random.choices(data, weights=weights, k=n)
    return randomlist
