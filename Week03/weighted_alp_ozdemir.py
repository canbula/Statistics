
import random 



def weighted_srs(data,n,weights,with_replacement:bool):

    if(with_replacement):
        return random.choices(data,weights=weights,k=n)
    else:
        return random.sample(data,n)

