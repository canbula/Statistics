import random
def weighted_srs(data, n, weights, with_replacement=False):
    data, w, res = list(data), (list(weights) if weights else None), []
    if with_replacement: return random.choices(data, weights=w, k=n)
    for _ in range(n):
        c = random.choices(data, weights=w, k=1)[0]; res.append(c)
        idx = data.index(c); data.pop(idx)
        if w: w.pop(idx)
    return res
