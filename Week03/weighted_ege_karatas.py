import random 

def weigthted_srs(data ,x , weights, with_replacement = False):
  if with_replacement == True  or  weights =! None:
     randomlist = random.choices( data , k = x , weights =  wights)
  else:
    randomlist =random.sample( data, x)
return randomlist
