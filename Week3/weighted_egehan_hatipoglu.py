import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement == True:
        return random.choices(data, weights=weights, k=n)
    else:
        sample = []
        copied_data = data.copy()
        copied_weights = weights.copy()
        for i in range(n):
            index = random.choices(range(len(copied_data)), weights=copied_weights, k=1)[0]
            sample.append(copied_data.pop(index))
            copied_weights.pop(index)
        return sample
