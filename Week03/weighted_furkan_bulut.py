import random
def weighted_srs(data,n,weights,with_replacement=False):
    if with_replacement or weights != None:
        return [random.choices(data,weights,k=n)]
    else:
        return random.choices(data,weights,k=n)
