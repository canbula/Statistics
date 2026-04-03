import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights is None:
        return random.choices(data, k=n) if with_replacement else random.sample(data, n)
    population = sum([[data[i]] * weights[i] for i in range(len(data))], [])
    return random.sample(population, n)