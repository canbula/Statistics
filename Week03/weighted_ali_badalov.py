import random

def weighted_srs(data, n, weights, with_replacment = False):
    if(with_replacment == True or weights != None): #Check if we are using replacement or not
        return random.choices(data, weights, k=n)
    else:
        return random.sample(data, n)
