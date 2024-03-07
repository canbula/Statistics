import random
def weighted_srs(data: list, n: int, weights=None, with_replacement=False):
    if with_replacement is not False or weights is not None:
        return [random.choices(data, k=n, weights=(weights if weights and len(weights) == len(data) else None))]
    return random.sample(data, min(n, len(data)))
