import random

def weighted_simple_random_sampling(data, n, weights, with_replacement=False):
    if with_replacement or weights is not None:
        return [random.choice(data, n, weights)]
    else:
        return [random.choice(data, n)]
