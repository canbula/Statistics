import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    result, data_copy, w_copy = [], data[:], weights[:]
    for _ in range(n):
        pick = random.choices(data_copy, weights=w_copy, k=1)[0]
        idx = data_copy.index(pick)
        result.append(data_copy.pop(idx))
        w_copy.pop(idx)
    return result