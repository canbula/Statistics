import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    sample, data, weights = [], list(data), list(weights)
    for _ in range(n):
        r = random.uniform(0, sum(weights))
        for i, w in enumerate(weights):
            r -= w
            if r <= 0: sample.append(data.pop(i)); weights.pop(i); break
    return sample
  
