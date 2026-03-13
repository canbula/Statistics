import random
def weighted_srs(data,n,weights,with_replacement=False):
    if weights is None:
        weights=[1]*len(data)
    if with_replacement or weights!=[1]*len(data):
        return random.choices(data,weights=weights,k=n)
    return random.sample(data,n)
