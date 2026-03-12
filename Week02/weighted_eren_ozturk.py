import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    sample, remaining_data, remaining_weights = [], list(data), list(weights)
    for _ in range(n):
        chosen_item = random.choices(remaining_data, weights=remaining_weights)[0]
        sample.append(chosen_item)
        remaining_weights.pop(remaining_data.index(chosen_item)); remaining_data.remove(chosen_item)
    return sample
