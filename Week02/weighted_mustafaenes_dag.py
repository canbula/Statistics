import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    sample, d, w = [], data[:], weights[:]
    for _ in range(n):
        chosen = random.choices(d, weights=w, k=1)[0]
        sample.append(chosen)
        idx = d.index(chosen); d.pop(idx); w.pop(idx)
    return sample
