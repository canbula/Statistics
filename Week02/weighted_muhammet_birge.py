import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    if not weights: return random.sample(data, n)
    res, pool = [], list(zip(data, weights))
    for _ in range(n):
        item = random.choices(pool, weights=[w for d, w in pool])
        res.append(item)
        pool.remove(item)
    return res
