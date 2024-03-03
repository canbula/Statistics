import random
def weighted_srs(data, n, weights, with_replacement=True):
    probabilities = [w/sum(weights) for w in weights]
    sampled_items = random.choices(data, probabilities, k=n) if with_replacement else random.sample(data, n)
    return sampled_items
