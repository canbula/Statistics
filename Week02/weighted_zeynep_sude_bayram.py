import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    result, d, w = [], list(data), list(weights)
    for _ in range(n):
        idx = random.choices(range(len(d)), weights=w, k=1)[0]
        result.append(d.pop(idx))
        w.pop(idx)
    return result
