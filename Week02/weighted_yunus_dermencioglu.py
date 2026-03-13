import random
def weighted_srs(data,n,weights,*,with_replacement=False):
    d,w,r=data[:],weights[:],[]  # copy lists so original data isn't modified
    for _ in range(n):
        x=random.uniform(0,sum(w)); s=0
        for i,v in enumerate(w):
            s+=v
            if s>=x: r.append(d[i]); break  # select item where random value falls
        if not with_replacement: d.pop(i); w.pop(i)
    return r
