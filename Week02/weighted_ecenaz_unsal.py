import random
def weighted_srs(data, n, weights, with_replacement=False):
    result=[]
    d=list(data); w=list(weights) if weights else [1]*len(data)
    for _ in range(n):
        x=random.choices(d, weights=w, k=1)[0]
        result.append(x)
        if not with_replacement:
            i=d.index(x); d.pop(i); w.pop(i)
    return result
