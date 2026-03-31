import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    d, w, s = data[:], weights[:], []
    for _ in range(n):
        i = random.choices(range(len(d)), weights=w, k=1)[0]
        s.append(d.pop(i)); w.pop(i)
    return s
