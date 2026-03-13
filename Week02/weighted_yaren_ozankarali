import random
def weighted_srs(data, n, weights, with_replacement = False):
  sample = []
  for i in range(n):
    index = random.choices(range(len(data)), weights=weights)[0]
    sample.append(data[index])
    if not with_replacement:
      data.pop(index)
      weights.pop(index)
  return sample
