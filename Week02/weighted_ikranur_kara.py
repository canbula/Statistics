import random
def weighted_srs(data,n,weights,with_replacement=False):
    if weights is None:
        return random.choices(data,k=n) if with_replacement else random.sample(data,n)
    if with_replacement:
        return random.choices(data,weights=weights,k=n)
    pop=[x for x,w in zip(data,weights) for _ in range(w)]
    return random.sample(pop,n)
