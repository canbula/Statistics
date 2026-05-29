import random
def weighted_srs(data, n, weights, with_replacement=False):
    w = [1]*len(data) if weights is None else weights
    if with_replacement: return random.choices(data, weights=w, k=n)
    res, d, ws = [], list(data), list(w)
    for _ in range(n):
        s = random.choices(d, weights=ws, k=1)[0]
        i = d.index(s); res.append(d.pop(i)); ws.pop(i)
    return res
