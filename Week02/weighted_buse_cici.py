import random
def weighted_srs(data, n, weights, with_replacement):
    if not with_replacement and n > len(data): return None
    sample, d, w = [], list(data), list(weights)
    for _ in range(n):
        c = random.choices(d, weights=w, k=1)[0]; sample.append(c)
        if not with_replacement:
            i = d.index(c); d.pop(i); w.pop(i)
    return sample
