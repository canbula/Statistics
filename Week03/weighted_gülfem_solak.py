import random
data = ["Pink","Blue","Purple","White","Black"]
n = 3
weights=[30,25,15,20,10]
with_replacement=True

def weighted_srs(data,n,weights,with_replacement):
    return random.choices(data,weights=weights,k=n)

print(weighted_srs(data,n,weights,True))
