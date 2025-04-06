import random
def weighted_srs(data, n, weights, with_replacement = False):
    if len(data) != len(weights):
        raise ValueError
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        if n > len(data):
            raise ValueError
        return random.sample(data, k=n)
