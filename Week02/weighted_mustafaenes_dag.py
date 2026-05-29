import random

def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement:
        # Ağırlıklı ve yerine koymalı (choices ağırlığı destekler)
        return random.choices(data, weights=weights, k=n)
    else:
        # Ağırlıklı ve yerine koymasız (sample ağırlığı destekler)
        return random.sample(data, counts=None, weights=weights, k=n)
