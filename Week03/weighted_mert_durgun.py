import random

def weighted_srs(data, n, weights, with_replacement = False):
    randomlist = random.choices(data, k=n, weights=weights) if weights != None or with_replacement == True else random.sample(data, n)
    return randomlist
