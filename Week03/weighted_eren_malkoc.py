import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        randomlist = random.sample(data, n)
    return randomlist
