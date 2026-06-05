import random
def weighted_srs(data: list, n: int, weights: list, with_replacement: bool = False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, k=n, counts=weights)
