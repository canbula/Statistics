import random

def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n) #sample with replacement
    if not weights: return random.sample(data, n) #simple random sample without weights
    return random.sample(data, n, counts=weights) #sample without replacement using weights as counts
