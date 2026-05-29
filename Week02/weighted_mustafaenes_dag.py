import random
def weighted_srs(data, n, weights=None, *, with_replacement=False):
    if weights is None:
        weights = [1] * len(data)    
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.sample(data, k=n) if all(w == weights[0] for w in weights) else \
               [val for val, weight in zip(data, weights) if weight > 0][:n]
