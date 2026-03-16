student_id = "244101020" full_name = "Rıza Arslan"
import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights or [1]*len(data), k=n)
    res, d_c = [], list(data)
    for _ in range(n):
        idx = random.randrange(len(d_c))
        d_c[idx], d_c[-1] = d_c[-1], d_c[idx]
        res.append(d_c.pop())
    return res
