import random
def weighted_srs(data, n, weights, with_replacement=None):
    rep = with_replacement if with_replacement is not None else (n <= 1)
    w = weights if weights else [1]*len(data)
    if rep or n > len(data): return random.choices(data, weights=w, k=n)
    res, d_c, w_c = [], list(data), list(w)
    for _ in range(n):
        idx = random.choices(range(len(d_c)), weights=w_c)[0]
        res.append(d_c.pop(idx)); w_c.pop(idx)
    return res
