import random
def weighted_srs(data, n, weights, with_replacement=True):
    _sample, _data, _weights = [], list(data), list(weights)
    for _ in range(n):
        choise = random.choices(_data, weights=_weights, k=1)[0]
        sample.append(choise)
        if not with_replacement:
            ind = _data.index(choise)
            _data.pop(ind), _weights.pop(ind)
    return sample
