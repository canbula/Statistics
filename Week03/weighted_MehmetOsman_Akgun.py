import random

def weighted_srs(data, n, weights, with_replacement=False):
    sampled = []
    while len(sampled) < n:
        choice = random.choices(data, weights=weights)[0]
        if with_replacement or choice not in sampled:
            sampled.append(choice)
    return sampled

