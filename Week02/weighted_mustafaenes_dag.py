import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    import numpy as np
    idx = np.random.choice(len(data), size=n, replace=False, p=np.array(weights)/sum(weights))
    return [data[i] for i in idx]
