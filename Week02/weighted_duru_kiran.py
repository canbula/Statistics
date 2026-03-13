import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    res, d, w = [], list(data), list(weights)
    for _ in range(n):
        index = random.choices(range(len(d)), weights=w, k=1)[0]
        res.append(d.pop(index))
        w.pop(index)
    return res
