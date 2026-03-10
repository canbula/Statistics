import random 

def weighted_srs(data,n,weights,with_replacement):
  if with_replacement == True: 
    return random.choices(data,weights=weights,k=n)
  else :
    return random.sample(data,k=n)
