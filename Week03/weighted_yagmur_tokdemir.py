import random

def weighted_srs(data, n, weights, with_replacement=False):
    normalized_weights = [weight / sum(weights) for weight in weights]
    sampled_data = random.choices(data, weights=normalized_weights, k=n) if with_replacement else random.sample(data, n)
    return sampled_data
