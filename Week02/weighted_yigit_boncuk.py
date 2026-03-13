import random


def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n) 
    result, d_copy, w_copy = [], list(data), list(weights)
    for _ in range(n):
        pick = random.choices(d_copy, weights=w_copy, k=1)[0] 
        idx = d_copy.index(pick) 
        result.append(d_copy.pop(idx)) 
        w_copy.pop(idx) 
    return result
