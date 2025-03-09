import random

def weighted_srs(data, n, weights, with_replacement):
    if(with_replacement): return random.choices(data, weights=weights, k=n )       
    else:     return random.sample(data, n)
population=['lawyer', 'engineer', 'student', 'driver', 'firefighter']
weights=[0.2, 0.5, 0.9, 0.7, 0.1]
sample=weighted_srs(population, 3, weights, True)
