import random

def weighted_srs(data, n, weights, with_replacement = False):
    if weights is not None:
        return random.choices(data, weights = weights, k = n)
    elif with_replacement == True:
        return random.choices(data, weights = weights, k = n)
    else:
        return random.sample(data, n)
