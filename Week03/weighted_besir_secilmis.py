import random

def weighted_srs(data, n, weights, with_replacement = False):

    if with_replacement == True or weights != None:
        sample = random.choice(data, k = n, weights = weights)
    else:
        sample = random.sample(data, n)
    return sample 
