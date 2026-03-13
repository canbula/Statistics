import random

def weighted_srs(data, n, weights, *, with_replacement=False):
    w, out = (weights[:] if weights else [1]*len(data)), []
    for _ in range(n):
        r = random.uniform(0, sum(w))
        for i in range(len(data)):
            r -= w[i]
            if r <= 0: out.append(data[i]); w[i] *= int(with_replacement); break
    return out