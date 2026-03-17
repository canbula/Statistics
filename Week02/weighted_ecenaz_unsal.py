import random
def weighted_srs(data,n,weights,*,with_replacement=False):
    if weights: return random.choices(data,weights=weights,k=n)
    result=[]; d=list(data)
    for _ in range(n):
        x=random.choice(d); result.append(x)
        if not with_replacement: d.remove(x)
    return result
