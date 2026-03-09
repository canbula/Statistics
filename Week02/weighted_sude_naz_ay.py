import random
def weighted_srs(data,n,weights,with_replacement=False):
    data=list(data); w=list(weights) if weights else None; res=[]
    for _ in range(n):
        c=random.choices(data,weights=w,k=1)[0]; res.append(c)
        if not with_replacement:
            i=data.index(c); data.pop(i)
            if w: w.pop(i)
    return res
