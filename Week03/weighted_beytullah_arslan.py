import random
def weighted_srs(data,n,weights,with_replacement=False):
  if with_replacement==True:
    return random.choices(data,weights=weights,t=n)

  return random.sample(data,n,counts=weights)
