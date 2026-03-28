import random
def weighted_srs(data, n, weights, with_replacement=False):
    if weights or with_replacement: return random.choices(data, weights=weights, k=n)
    sample, re_data = [], list(data)
    for _ in range(n):
        choisen = random.choices(re_data)[0]
        sample.append(choisen)
        re_data.remove(choisen)
    return sample
