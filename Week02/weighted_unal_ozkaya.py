import random
def weighted_srs(data: list,n: int,weights: list,with_replacement: bool=False):
  if with_replacement:
    return random.choices(population=data,weights=weights,cum_weights=None,k=n)
  return random.sample(population=data,k=n,counts=weights)
