import random

def weighted_srs(data, n, weights, with_replacement):
  sample = []
  if (with_replacement):
    sample = random.choices(data, weights, k=n)
  else:
    sample = random.sample(data, n, counts=weights)
  return sample
