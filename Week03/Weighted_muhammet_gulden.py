import random

def weighted_srs(data, n, weights, with_replacement):
    return random.choices(data, weights=weights, k=n) if with_replacement else random.sample(data, n)

data = ['A', 'B', 'C', 'D']
weights = [10, 5, 3, 1]
n = 2
print(weighted_srs(data, n, weights, True))
print(weighted_srs(data, n, weights, False))
