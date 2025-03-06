import random

def weighted_srs(data, n, weights, with_replacement = False):
    if weights is not None:
         return random.choices(data, k=n, weights=weights)
    elif with_replacement: 
         return random.choices(data, n)
    else:
        return random.sample(data, n)
