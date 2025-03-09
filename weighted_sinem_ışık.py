import random 
def weighted_srs(data, n, weights, with_replacement): 
    return random.choices(data, weights=weights, k=n) if 
  data = ['sinem', 'muhammet', 'selim', 'seher'] 
weights = [11, 23, 9, 7] 
n = 2 
print(weighted_srs(data, n, weights, True)) 
print(weighted_srs(data, n, weights, False)) 
