import random

def weighted_srs(data, n, weights = None, with_replacement = False):
    if weights == None and with_replacement == False:
        return random.sample(data, n)
    else:
        return random.choices(data,  weights = weights, k = n)
