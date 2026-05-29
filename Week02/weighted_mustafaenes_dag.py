import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    k = min(n, len(data))
    return random.sample(data, k=k, counts=[int(w * 1000) for w in weights])
