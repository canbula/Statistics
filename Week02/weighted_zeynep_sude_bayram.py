import random

def weighted_srs(data, n, weights, with_replacement):
    result = []
    d_list = list(data)
    w_list = list(weights)
    
    for _ in range(n):
        chosen = random.choices(d_list, weights=w_list, k=1)[0]
        result.append(chosen)
        
        if not with_replacement:
            idx = d_list.index(chosen)
            d_list.pop(idx)
            w_list.pop(idx)
            
    return result
