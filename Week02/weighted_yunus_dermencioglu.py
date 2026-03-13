import random

def weighted_srs(data, n, weights, with_replacement=True):
    if with_replacement: return random.choices(data, weights=weights, k=n)  # allows repeats
    w, res = list(weights), []
    for _ in range(n):
        i = random.choices(range(len(data)), weights=w)[0]  # pick by current weights
        res.append(data[i]); w[i] = 0
    return res
