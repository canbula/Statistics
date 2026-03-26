import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement == True: return random.choices(data, weights=weights, k=n)
    sample = []
    copied_data, copied_weights = data.copy(), weights.copy()
    for i in range(n):
        index = random.choices(range(len(copied_data)), weights=copied_weights, k=1)[0]
        sample.append(copied_data.pop(index))
        copied_weights.pop(index)
    return sample
