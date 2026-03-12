import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    res, d, w = [], list(data), list(weights)
    for _ in range(n):
        i = d.index(random.choices(d, weights=w)[0])
        res.append(d.pop(i))
        w.pop(i)
    return res
