import random

def weighted_srs(data, n, weights=None, with_replacement=False):
  if with_replacement: return random.choices(data, weights=weights, k=n)
  result, pool, w = [], list(data), (list(weights) if weights else None)
  for _ in range(n):
      i = random.choices(range(len(pool)), weights=w, k=1)[0] if w else random.randrange(len(pool))
      result.append(pool.pop(i))
      if w: w.pop(i)
  return result
