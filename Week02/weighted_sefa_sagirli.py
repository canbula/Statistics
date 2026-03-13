import random 
def weighted_srs(data, n, weigths, with_replacement):
  if with_replacement == True: return random.choices(data, weights=weights, k=n)
    = list(weights)
result = []
for i in range(n):
  chosen_index = random.choices(range(len(data)), weigths = copy, k=1)[0] 
result.append(data[chosen_index])
copy[chosen_index] = 0
return result
