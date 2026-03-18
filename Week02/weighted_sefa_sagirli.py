import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    newList, result = list(weights), []
    for i in range(n):
        idx = random.choices(range(len(data)), weights=newList, k=1)[0]
        result.append(data[idx])
        newList[idx] = 0
    return result
