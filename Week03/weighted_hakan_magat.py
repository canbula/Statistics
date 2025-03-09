import random  #random

def weighted_srs(data, n, weights, with_replacement = False):
    if with_replacement == True or weights != None:
        randomlist = random.choices(data, k = n, weights = weights)
    else:
        randomlist = random.sample(data, n)
    return randomlist
