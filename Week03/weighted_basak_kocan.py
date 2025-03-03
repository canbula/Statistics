import random

def weighted_srs(data, n, weights, with_replacement = False):
weighted_srs_sample = random.choices(data, weights, k=n)
if weights != None or with_replacement == True
else random.sample(data, n)
return weighted_srs_sample
