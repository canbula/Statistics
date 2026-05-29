import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    res = set()
    while len(res) < n:
        choice = random.choices(data, weights=weights, k=1)[0]
        res.add(choice)
    return list(res)
