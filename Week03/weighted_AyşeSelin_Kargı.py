import random
def weight_srs(data , n,weights, with_replacement = False):
    if with_replacement == True or weights is not None:
        random_list= random.choices(data , k=n, weights=weights)
    else:
        random_list=random.sample(data,n)
    return random_list
