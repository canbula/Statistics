 import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        res = []
        while len(res) < n:
            val = random.choices(data, weights=weights, k=1)[0]
            if val not in res: res.append(val)
        return res
