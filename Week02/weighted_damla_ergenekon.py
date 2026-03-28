import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    if not weights: return random.sample(data, n)
    indexes = []
    while len(indexes) < n:
        i = random.choices(range(len(data)), weights=weights)[0]
        if i not in indexes: indexes.append(i)
    return [data[i] for i in indexes]
