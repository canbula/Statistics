import random 

def weighted_srs(data, x, weights=None, with_replacement=False):
    if with_replacement or weights is not None:
        random_list = random.choices(data, k=x, weights=weights)
    else:
        random_list = random.sample(data, x)
    return random_list

