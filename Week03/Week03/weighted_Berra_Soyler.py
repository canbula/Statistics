import random
def weighted_srs(data, int n, weights, with_replacement):
  if with_replacement == True:
      return [random.choices(data, weights, k=1)[0] for _ in range(n)]
  else:
      return random.sample(data, n)
