import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n) # If sampling with replacement, we can directly use random.choices
    w, res = list(weights), []
    for _ in range(n):
        idx = random.choices(range(len(data)), weights=w)[0] # choose an index based on the current weight distribution
        res.append(data[idx])
        w[idx] = 0
    return res
