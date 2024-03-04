import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement == True or weights != None:
         sample_list = random.choices(data, k=n, weights=weights)
    else:
         sample_list = random.sample(data,n)
    return sample_list

