import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    selected, w = [], list(weights)
    for _ in range(n):
        index = random.choices(range(len(data)), weights=w)[0]
        selected.append(data[index])
        w[index] = 0
    return selected
