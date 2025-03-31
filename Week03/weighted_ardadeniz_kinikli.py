import random 
def weighted_srs(data,n,weights,with_replacement=False){
    if with_replacement==True and weights != None:
        simple_sample = random.choices(data,weights=weights, k=n)
    else:
        simple_sample = random.sample(data,n)
    return simple_sample
}
