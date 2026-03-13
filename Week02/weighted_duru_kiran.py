import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights: return random.choices(data, weights=weights, k=n)
    res, temp_data = [], list(data)
    for _ in range(n):
        target_index = random.randrange(len(temp_data))
        res.append(temp_data.pop(target_index))
    return res
