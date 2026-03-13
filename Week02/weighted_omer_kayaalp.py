import random
def weighted_srs(data,n , weights, with_replacement=False):
    d, w = list(data), list(weights)
    if with_replacement: return random.choices(d, weights=w, k=n)
    res = []
    for _ in range(min(n, len(d))):
        idx = random.choices(range(len(d)), weights=w, k=1)[0]
        res.append(d.pop(idx)); w.pop(idx)
    return res
