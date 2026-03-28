import random
def weighted_srs(data, n, weights, *, with_replacement=True):
    sample, d, w = [], list(data), list(weights)
    for _ in range(n):
        choise = random.choices(d, weights=w, k=1)[0]
        sample.append(choise)
        if not with_replacement: ind = d.index(choise); d.pop(ind); w.pop(ind)
    return sample
