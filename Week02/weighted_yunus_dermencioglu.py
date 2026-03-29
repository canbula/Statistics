import random

def weighted_srs(data, n, weights, *args, with_replacement=False):
    if args: with_replacement = args[0]  # also accept 4th positional arg if given
    if with_replacement: return random.choices(data, weights=weights, k=n)  # repeats allowed
    w, res = list(weights), []
    for _ in range(n):
        i = random.choices(range(len(data)), weights=w)[0]
        res.append(data[i]); w[i] = 0
    return res
