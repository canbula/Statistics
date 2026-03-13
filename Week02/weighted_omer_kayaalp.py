def weighted_srs(data, weights, n, *, with_replacement=False):
    import random
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    r=[]; d=data[:]; w=weights[:]
    for _ in range(n):
        i=random.choices(range(len(d)), weights=w)[0]
        r.append(d.pop(i)); w.pop(i)
    return r
