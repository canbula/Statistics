import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)  # sampling with replacement
    w, res = list(weights), []
    for _ in range(n):
        idx = random.choices(range(len(data)), weights=w)[0]  # pick index based on weights
        res.append(data[idx])
        w[idx] = 0
    return res
