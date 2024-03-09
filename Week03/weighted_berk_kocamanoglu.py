import random

def weighted_srs(data , n , weights , with_replacement = False):
    if with_replacement or weights == None: 
        return random.sample(data , n)
    else:
        random_list = random.choices(data , weights=weights , k=n)
        return random_list
