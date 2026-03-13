import random
def weighted_srs(data, n, weights=None, *, with_replacement=False):
    w, s = list(weights) if weights else [1]*len(data), []
    if with_replacement: return random.choices(data, weights=w, k=n)
    for _ in range(n):
        idx = random.choices(range(len(data)), weights=w)[0]
        s.append(data[idx])
        w[idx] = 0
    return s
