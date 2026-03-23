import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    sample, d, w = [], data[:], weights[:]
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w , k = 1)[0]
        sample.append(d.pop(i))
        w.pop(i)
    return sample
