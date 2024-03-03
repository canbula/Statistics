import random
def weighted_srs(data, n, weights, with_replacement=True):
    probabilities = [w/sum(weights) for w in weights]
    sampled_items = random.choices(data, probabilities, k=n) if with_replacement else random.sample(data, n)
    return sampled_items
population, sample_size, weights = ["A", "B", "C", "D"], 3, [0.2, 0.3, 0.4, 0.1]
result = weighted_srs(population, sample_size, weights, with_replacement=True)
print("Weighted Random Sample:", result)
