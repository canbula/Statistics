import random
def weighted_srs(data, weights, n, with_replacement=False):
    d, w = list(data), list(weights)
    if with_replacement:
        return random.choices(d, weights=w, k=n)
    res = []
    for _ in range(min(n, len(d))):
        i = random.choices(range(len(d)), weights=w)[0]
        res.append(d.pop(i)); w.pop(i)
    return res
