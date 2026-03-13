import random
def weighted_srs(data, n, weights, with_replacement=False):
    data, weights, result = list(data), list(weights), []
    for _ in range(n):
        idx = random.choices(range(len(data)), weights=weights, k=1)[0]
        result.append(data[idx])
        if not with_replacement:
            data.pop(idx); weights.pop(idx)
    return result
