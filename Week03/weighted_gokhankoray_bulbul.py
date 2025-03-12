import random

def weighted_srs(data, n, weights, with_replacement):
  Sample = []
  if (with_replacement):
    Sample = random.choices(data, weights, k=n)
  else:
    Sample = random.sample(data, n, counts=weights)
  return Sample
