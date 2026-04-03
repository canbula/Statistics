import statistics
def weighted_srs(data, n, weights, with_replacement=False):
    if weights is None:
        return random.choices(data, k=n) if with_replacement else random.sample(data, n)
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    population = sum([[d]*w for d, w in zip(data, weights)], [])
    return random.sample(population, n)
