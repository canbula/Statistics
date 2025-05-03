import random

def weighted_srs(data,n,weights,with_replacement=True):
    if with_replacement:
        return random.choices(data,k=n,weights=weights)
    else:
        return random.sample(data, n)
        
