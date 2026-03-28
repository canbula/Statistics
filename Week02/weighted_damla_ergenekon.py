import random

def weighted_srs(data, n, weights, with_replacement=False):
    if weights is None and with_replacement is False:
        sample_list = random.sample(data, n)
    else:
        sample_list = random.choices(data, weights=weights, k=n)
    return sample_list
