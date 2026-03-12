import random
def weighted_srs(data,n,weights,with_replacement):
    d,w,r=data[:],weights[:],[]
    for _ in range(n):
        x=random.uniform(0,sum(w)); s=0
        for i,v in enumerate(w):
            s+=v
            if s>=x: r.append(d[i]); break
        if not with_replacement: d.pop(i); w.pop(i)
    return r
