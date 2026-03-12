import random
def weighted_srs(data , n, weights,with_replacement) :
    if with_replacement : return random.choices(data , weights=weights , k=n)
    result , d , w = [] , list(data) , list(weights)
    for _ in range(n) :
       choosen = random.choices(d , weights=w , k=1)[0]
       x = d.index(choosen)
       result.append(d.pop(x))
       w.pop(x)
    return result
