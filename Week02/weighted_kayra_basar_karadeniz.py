import random
def weighted_srs(data, n, weights, with_replacement=False):
    res, d_copy, w_copy = [], list(data), list(weights) if weights else [1]*len(data)
    for _ in range(n):
        idx = random.choices(range(len(d_copy)), weights=w_copy)[0]
        res.append(d_copy[idx] if with_replacement else d_copy.pop(idx))
        if not with_replacement: w_copy.pop(idx)
    return res
