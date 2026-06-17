import random
def weighted_srs(data,n,weights,with_replacement=False):
    if with_replacement == True:return random.choices(data,k=n,weights=weights)      
    res,d_cp,w_cp=[],list(data),list(weights) if weights else None
    for _ in range(n):
        v = random.choices(d_cp,k=1,weights = w_cp)[0]
        if w_cp:w_cp.pop(d_cp.index(v))  
        res.append(d_cp.pop(d_cp.index(v)))
    return res 
