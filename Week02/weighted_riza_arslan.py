student_id = "244101020"
full_name = "Rıza Arslan"
import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        return random.choice(data, weights=None, k=n)
        
    
