import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    res, temp_w = [], list(weights)
    for _ in range(n):
        i = random.choices(range(len(data)), weights=temp_w)[0]
        res.append(data[i]); temp_w[i] = 0
    return res
