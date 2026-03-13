import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    res, d, w = [], list(data), list(weights)
    for _ in range(n):
        p = random.choices(d, weights=w, k=1)[0]; i = d.index(p)
        res.append(d.pop(i)); w.pop(i)
    return res 
