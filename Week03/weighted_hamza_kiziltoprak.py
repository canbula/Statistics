import random
def weighted_srs(data, n, weights, with_replacement = False):
    sample = random.choices(data, weights=weights, k=n) if with_replacement  or weights != None else random.sample(data, n)
    return sample
