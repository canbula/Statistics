import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    if not weights: return random.choices(data, k=n) if with_replacement else random.sample(data, n)
    if with_replacement: return random.choices(data, weights=weights, k=n)
    d, w, res = list(data), list(weights), []
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w, k=1)[0]
        res.append(d.pop(i)); w.pop(i)
    return res
