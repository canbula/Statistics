student_id = "244101020"
full_name = "Rıza Arslan"
import random
def weighted_srs(data, n, weights, with_replacement=False):
    w = weights if weights else [1]*len(data)
    if with_replacement or weights:
        return random.choices(data, weights=w, k=n)
    res, d_c = [], list(data)
    for _ in range(n): res.append(d_c.pop(random.randrange(len(d_c))))
    return res:
