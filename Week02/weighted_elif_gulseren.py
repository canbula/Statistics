import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement is True: return random.choices(data, weights=weights, k=n)
    res, w, d = [], list(weights), list(data)
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w)[0]
        res.append(d[i])
        w[i] = 0
    return res
