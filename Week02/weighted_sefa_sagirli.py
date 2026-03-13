import random 
def weighted_srs(data, n, weights, with_replacement):
  if with_replacement == True: return random.choices(data, weights=weights, k=n)
  newList = list(weights)
result = []
for i in range(n):
  chosen_index = random.choices(range(len(data)), weigths = newList, k=1)[0] 
result.append(data[chosen_index])
newList[chosen_index] = 0
return result
