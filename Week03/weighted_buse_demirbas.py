import random
def weighted_srs(data , n , weights , with_replacement=True):
    if with_replacement == True and weights is not None:
      return  random.choices (data , weights = weights , k=n) 
    else:
       return random.sample(data , n)
