import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n) #easy path if replacement is on
    d, w, sample = data[:], weights[:], [] #we make copies so we don't mess up the original data
    for _ in range(n):
        i = d.index(random.choices(d, weights=w)[0]) #pick one based on weights and find its index
        sample.append(d.pop(i)) #put it in the sample list remove from data
        w.pop(i) #remove the matching weight so we don't break the balance
    return sample
