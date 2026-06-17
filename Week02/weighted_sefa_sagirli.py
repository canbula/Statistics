import random
def weighted_srs(data, n, weights, with_replacement = False):
    if not (with_replacement or weights):
        sample = random.sample(data, n)
    else:
        sample = random.choices(data, weights=weights, k=n)
    return sample
