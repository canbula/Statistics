import random

def weighted_srs(data, n, weights, with_replacement):
    sample = []
    if with_replacement:
        sample.append(random.choices(data, weights, k=n))
    else:
        sample.append(random.sample(data, n))
return sample
