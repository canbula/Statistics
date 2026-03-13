import random

def weighted_srs(data, n, weights, with_replacement):
    w, out = list(weights) if weights else [1] * len(data), []
    for _ in range(n):
        target, current = random.uniform(0, sum(w)), 0
        for i, val in enumerate(w):
            current += val
            if target <= current: out.append(data[i]); w[i] *= int(with_replacement); break
    return out
