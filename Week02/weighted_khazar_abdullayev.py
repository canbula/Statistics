import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    s, w = [], list(weights)
    for _ in range(n):
        idx = random.choices(range(len(data)), weights=w)[0]
        s.append(data[idx])
        w[idx] = 0
    return s
