import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    if weights is None: weights = [1] * len(data)
    population, _weights, sample = list(data), list(weights), []
    while len(sample) < n:
        picked = random.choices(population, weights=_weights, k=1)[0]
        if with_replacement or picked not in sample: sample.append(picked)
    return sample
