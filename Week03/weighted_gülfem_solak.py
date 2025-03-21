import random
def weighted_srs(data,n,weights,with_replacement=True):
    if with_replacement:
        return random.choices(data,k=n,weights=weights)
    else:
        return random.sample(data, n)
data = ["Pink","Blue","Purple","White","Black"]
n = 3
weights=[30,25,15,20,10]
print(weighted_srs(data,n,weights,True))
