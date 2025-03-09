import random
def weighted_srs(data, n, weights, with_replacement):
    return random.choices(data, weights=weights, k=n) if with_replacement==True else random.sample(data, k=n)
