import random

def weighted_srs(data, n, weights, with_replacement):
    if not with_replacement and n > len(data):
        raise ValueError("The sample size without replacement cannot be larger than the population!")

    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.sample(data, n)

try:
    sample = weighted_srs(['Elif', 'Kenan', 'Sırma', 'Dilara', 'Murat'], 3, [0.2, 0.2, 0.2, 0.2, 0.2], False)
    sample2 = weighted_srs(['Elif', 'Kenan', 'Sırma', 'Dilara', 'Murat'], 3, [0.1, 0.3, 0.2, 0.25, 0.15], True)
    print("Chosen sample:", sample)
    print("Chosen sample:", sample2)
except ValueError as e:
    print("Error:", e)
