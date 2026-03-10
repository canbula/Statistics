def weighted_srs(data, n, weights, with_replacement):
    import random
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    res=[]
    d=data[:]; w=weights[:]
    for _ in range(n):
        i=random.choices(range(len(d)), weights=w, k=1)[0]
        res.append(d.pop(i)); w.pop(i)
    return res
