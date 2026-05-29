import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    res = []
    for _ in range(n):
        s = random.choices(data, weights=weights, k=1)[0]
        i = data.index(s)
        res.append(data.pop(i))
        weights.pop(i)
    return res
