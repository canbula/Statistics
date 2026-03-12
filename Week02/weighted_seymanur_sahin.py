import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    result, temp_data, temp_weights = [], list(data), list(weights)
    for _ in range(n):
        chosen_item = random.choices(temp_data, weights=temp_weights, k=1)[0]
        target_index = temp_data.index(chosen_item)
        result.append(temp_data.pop(target_index))
        temp_weights.pop(target_index)
    return result
