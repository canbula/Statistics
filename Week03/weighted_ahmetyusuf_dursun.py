import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement or weights !=None:
        randomsample=random.choices(data, k=n, weights=weights)
    else:
        randomsample=random.sample(data,n)
    return randomsample
