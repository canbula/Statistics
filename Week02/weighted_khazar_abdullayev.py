import random

def weighted_srs(data, n, weights, with_replacement=False):
    use_choices = bool(with_replacement or weights)
    if use_choices:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, n)
