import random

def weighted_srs(data, n, weights, with_replacement = False):

    if(with_replacement is True):
        sample = random.choices(data, weights=weights, k=n)
    else:
        sample = random.sample(data, n)

    return sample    
        
