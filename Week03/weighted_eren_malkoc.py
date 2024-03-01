import random

def weighted_srs(data, n, weights=None, *, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights, k=n)
    choices, actual_weights = list(data), list(weights) if weights else [1] * len(data)
    return [choices.pop(i) for i in [actual_weights.pop(choices.index(random.choices(choices, actual_weights, k=1)[0])) for _ in range(n)]]
