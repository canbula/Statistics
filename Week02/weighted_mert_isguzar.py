import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    if not weights: return random.sample(data, n)
    d, w, res = list(data), list(weights), []
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w)[0]
        res.append(d.pop(i))
        w.pop(i)
    return res
