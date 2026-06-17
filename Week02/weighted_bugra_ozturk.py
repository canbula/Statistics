import random

def weighted_srs(data, n, weights, with_replacement):
    total = sum(weights)
    normalized = [w / total for w in weights]
    if with_replacement:
        cumulative = [sum(normalized[:i+1]) for i in range(len(normalized))]
        sample = []
        for _ in range(n):
            r = random.random()
            sample.append(data[next(i for i, c in enumerate(cumulative) if r <= c)])
        return sample
    return random.sample(data, n, counts=[round(w*1000) for w in normalized])
