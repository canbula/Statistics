import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement is not False or weights is not None:
        return [random.choices(data, k=n, weights=weights)]
    return random.sample(data, n)
