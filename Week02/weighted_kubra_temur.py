import random


def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    
    result = []
    temp_data, temp_weights = list(data), list(weights)
    for _ in range(n):
        pick = random.choices(temp_data, weights=temp_weights, k=1)[0]
        idx = temp_data.index(pick)
        result.append(temp_data.pop(idx))
        temp_weights.pop(idx)
    return result
