import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if weights is None: weights = [1] * len(data)
    total = sum(weights)
    normalized = [w / total for w in weights]
    cumulative = [sum(normalized[:i+1]) for i in range(len(normalized))]
    sample = []
    while len(sample) < n:
        r = random.random()
        picked = data[next(i for i, c in enumerate(cumulative) if r <= c)]
        if with_replacement or picked not in sample: sample.append(picked)
    return sample
