import random

def weighted_srs(data, n, weights, with_replacement = False):
    if weights != None or with_replacement == True:
        return random.choices(data, k=n, weights=weights)
    else:
        return random.sample(data, n)
