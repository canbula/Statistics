def weighted_srs(population, weights, k, *, with_replacement=False):
    import random
    if with_replacement:
        return random.choices(population, weights=weights, k=k)
    r=[]; p=population[:]; w=weights[:]
    for _ in range(k):
        i=random.choices(range(len(p)), weights=w)[0]
        r.append(p.pop(i)); w.pop(i)
    return r
