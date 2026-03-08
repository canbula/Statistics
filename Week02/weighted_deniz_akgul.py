import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    d, w, res = list(data), list(weights) if weights else None, []
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w)[0]
        res.append(d.pop(i))
        if w is not None: w.pop(i)
    return res
