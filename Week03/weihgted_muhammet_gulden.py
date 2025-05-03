import random

def weighted_srs(data, n, weights, with_replacement):
    return random.choices(data, weights=weights, k=n) if with_replacement else random.sample(data, n)

data = ['sinem', 'muhammet', 'arzu', 'tahir']
weights = [11, 23, 9, 5]
n = 2
print(weighted_srs(data, n, weights, False))
print(weighted_srs(data, n, weights, True))
