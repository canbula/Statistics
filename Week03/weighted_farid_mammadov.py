import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        total_samples = min(len(data), n)
        return random.sample([random.choices(data, weights=weights, k=1)[0] for _ in range(total_samples)], k=total_samples)
data_population = ['A', 'B', 'C', 'D', 'E']
sample_size = 3
weights_for_population = [10, 1, 1, 1, 1]
with_replacement_flag = True
sample = weighted_srs(data_population, sample_size, weights_for_population, with_replacement_flag)
print(sample)
