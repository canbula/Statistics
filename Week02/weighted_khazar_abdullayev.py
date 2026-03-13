import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    w = [1] * len(data) if weights is None else weights[:]
    sample = []
    for _ in range(n):
        r = random.uniform(0, sum(w))
        for i in range(len(data)):
            r -= w[i]
            if r <= 0: sample.append(data[i]); w[i] = w[i] if with_replacement else 0; break
    return sample
