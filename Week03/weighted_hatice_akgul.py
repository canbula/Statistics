import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        random_sample = random.choices(data, weights=weights, k=n)
    else:
        random_sample = random.sample(data, n)
    return random_sample
