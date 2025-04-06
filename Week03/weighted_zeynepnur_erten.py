import random

def weighted_srs(data,n,weights,with_replacement):
    if(with_replacement==True):
        return random.sample(data,n)
    else:
        return random.choice(data,weights,n)


