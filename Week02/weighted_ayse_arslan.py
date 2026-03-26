import random  #
def weighted_srs(data, n, weights, with_replacement=False):
    if weights==None:
        return random.choices(data,k=n) if with_replacement else random.sample(data,n)
    if with_replacement: return random.choices(data,weights=weights,k=n)
    s=[]
    while len(s)<n:
        c=random.choices(data,weights=weights)[0]
        if c not in s: s.append(c)
    return s
