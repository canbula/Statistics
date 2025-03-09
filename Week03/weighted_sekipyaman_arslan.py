import random

def weighted_srs(data, n, weights, with_replacement):
  if with_replacement:
    return random.choices(data, weights=weights, k=n)
  else:
    return list(set(random.choices(data, weights=weights, k=n)))
    
  
