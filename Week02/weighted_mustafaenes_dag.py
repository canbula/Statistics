import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.sample(data,n)
