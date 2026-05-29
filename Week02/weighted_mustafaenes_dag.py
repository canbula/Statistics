import random

def weighted_srs(data, n, weights, with_replacement=True):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    for _ in range(n):
        res.append(random.choices(data, weights=weights, k=1)[0])
    return res
