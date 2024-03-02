import random

def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        total_samples = min(len(data), n)
        return random.sample([random.choices(data, weights=weights, k=1)[0] for _ in range(total_samples)], k=total_samples)
