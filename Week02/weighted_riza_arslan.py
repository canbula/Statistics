student_id = "244101020"
full_name = "Rıza Arslan"
import random
def weighted_srs(data, n, weights, with_replacement=True):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.sample(data, n, weights=weights)
    