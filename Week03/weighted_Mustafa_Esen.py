import random
def simple_random_sampling(data, n, weights, with_replacement=True):
    if len(weights) != len(data):
        sampled_data = random.choices(weights, k=n)
    else:
        sampled_data = random.sample(weights, n)
    return sampled_data
