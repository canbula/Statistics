import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(d, weights=w, k=n)
res,d, w = [], list(data), list(weights)
    for _ in range(min(n, len(d))):
        idx = random.choices(range(len(d)), weights=w)[0]
        res.append(d.pop(idx)); w.pop(idx)
    return res
