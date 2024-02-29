import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights, k=n)
    else: 
        sample = []
        for _ in range(n):
            chosen = random.choices(data, weights, k=1)[0]
            sample.append(chosen)
            index = data.index(chosen)
            data.pop(index)
            weights.pop(index)
        return sample
