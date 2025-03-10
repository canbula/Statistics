import random
def  weighted_srs(data,n,weights, with_replacement=False):
    if weights is None and not with_replacement:
        return random.sample(data,n)
    return random.choices(data, weights= weights, k=n )
