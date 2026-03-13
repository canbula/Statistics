import random 
def weighted_srs(data,n,weights,with_replacement):
    res=[]
    d=list(data); w=list(weights)
    for _ in range(n):
        i=random.choices(range(len(d)),weights=w,k=1)[0]
        res.append(d[i])
        if not with_replacement:
            d.pop(i); w.pop(i)
    return res
