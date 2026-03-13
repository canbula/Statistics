import random
def weighted_srs(data, n, weights, with_replacement=False):
    if weights or with_replacement: return random.choices(data, weights=weights, k=n)
    sample, remaining_data = [], list(data)
    for _ in range(n):
        chosen = random.choices(remaining_data)[0]
        sample.append(chosen)
        remaining_data.remove(chosen)
    return sample
