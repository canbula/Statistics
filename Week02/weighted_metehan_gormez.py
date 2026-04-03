import random

def weighted_srs(data, n, weights, with_replacement=False):
    if weights and with_replacement:
        return random.choices(data, weights=weights, k=n)
    elif weights:
        return random.sample(data, counts=[int(w*100) for w in weights], k=n)
    return random.choices(data, k=n) if with_replacement else random.sample(data, n)
