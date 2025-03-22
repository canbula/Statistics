import random

def weighted_srs(data, n, weights, with_replacement=True):
  
     return random.sample(data,n) if with_replacement==False and weights==None  else return random.choices(data,k=n,weights=weights)
    

    
   
