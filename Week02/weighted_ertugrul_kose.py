import random

def weighted_srs(dataset, k, w, with_replacement=False):
    if with_replacement or w:
        return random.choices(dataset, weights=w, k=k)
    else:
        return random.sample(dataset, k)
