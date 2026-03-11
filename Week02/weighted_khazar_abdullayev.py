import random

def weighted_srs(data, n, weights, with_replacement):
    total_weight = sum(weights)
    probabilities = [w / total_weight for w in weights]
    sample = random.choices(data, weights=probabilities, k=n, replace=with_replacement)
    return sample
