import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    counts = [int(w * 10000) + 1 for w in weights] if weights else None
    return random.sample(data, counts=counts, k=n) if weights else random.sample(data, n)
