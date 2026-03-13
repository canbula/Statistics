import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    sample=[]     #for picking without replacement
    d=data[:]; w=weights[:]
    for _ in range(n):   #we need to pick n items in total
        x=random.choices(d, weights=w, k=1)[0]   #grab just 1 item based on the current weights
        i=d.index(x); sample.append(x); d.pop(i); w.pop(i)   #find it, add to our sample, and pop it out so it doesn't get picked again
    return sample
