import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    if not weights: return random.sample(data, n)
    res = []
    while len(res) < n:
        item = random.choices(data, weights=weights, k=1)[0]
        if item not in res: res.append(item)
    return res
