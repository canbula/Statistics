import random


def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    
    result = []
    temp_data, temp_weights = list(data), list(weights)
    for _ in range(n):
        choice = random.choices(range(len(temp_data)), weights=temp_weights, k=1)[0]
        result.append(temp_data.pop(choice))
        temp_weights.pop(choice)
    return result
