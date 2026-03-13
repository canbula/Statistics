import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    res, d, w = [], list(data), list(weights)
    for _ in range(n):
        pick = random.choices(d, weights=w, k=1)[0]
        idx = d.index(pick)
        res.append(d.pop(idx))
        w.pop(idx)
    return res result
   
