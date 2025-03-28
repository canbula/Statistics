import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement == True or weights!=None:
         random.choices(data, k=n , weights=weights )       
    else:    
         random.sample(data, n)
return sample
