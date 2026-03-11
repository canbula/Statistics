import random
def weighted_srs(data, n, weights, with_replacement):
  result = []
  for i in range(n):
    idx = data.index(random.choices(data, weights=weights, k=1)[0])
    result.append(data[idx])
    if not with_replacement:
      data.pop(idx)
      weights.pop(idx)
  return result
