import random

def weighted_srs(data, n, weights, *args, with_replacement=False):
    if args: with_replacement = args[0]
    if with_replacement: 
        return random.sample(data, k=n)
    
    w = weights if weights else [1] * len(data)
    return random.choices(data, weights=w, k=n)
