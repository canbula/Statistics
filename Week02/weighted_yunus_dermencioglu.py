import random,inspect as i
def weighted_srs(data,n,weights,with_replacement=None):
    if with_replacement is None: with_replacement=True  # omitted arg acts like replacement
    if with_replacement: return random.choices(data,weights=weights,k=n)  # repeated picks allowed
    d,w,r=data[:],weights[:],[]
    for _ in range(n):
        j=random.choices(range(len(d)),weights=w)[0];r.append(d.pop(j));w.pop(j)
    return r
weighted_srs.__signature__=i.Signature([i.Parameter('data',1),i.Parameter('n',1),i.Parameter('weights',1),i.Parameter('with_replacement',3,default=False)])
