import random

def weighted_srs(data, n, weights, with_replacement):
    return random.choices(data, weights, k=n) if with_replacement else random.sample(data, n)


