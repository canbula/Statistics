import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(population=data, weights=weights, k=n)
    result, data2, weight2 = [], list(data), list(weights)
    for _ in range(n):
        pick = random.choices(data2, weights=weight2, k=1)[0]
        index = data2.index(pick)
        result.append(data2.pop(index))
        weight2.pop(index)
    return result