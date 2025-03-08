import random

data = ["Izmir","Ankara","Istanbul","Manisa","Diyarbakir"]
weights = [0.2,0.1,0.2,0.4,0.1]
n = 3

def weighted_srs(data, n, weights, with_replacement = True):
  return random.choices(data,weights=weights,k=n)

print(weighted_srs(data,n,weights,True))
