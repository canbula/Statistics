import random

def weighted_srs(data , n , weights , with_replacement = False):
    if with_replacement or weights == None: 
        sample = random.sample(data , n)
    else:
        sample = random.choices(data , weights=weights , k=n)
    return sample
