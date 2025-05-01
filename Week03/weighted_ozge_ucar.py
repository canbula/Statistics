import random
data = ['a','b','c','d','e']
weights=[0.1, 0.2, 0.7, 0.9, 0.3]
def weight_srs(data , n,weights, with_replacement = False):
    if with_replacement == True or weights != None:
        random_list= random.choices(data , k=n, weights=weights)
    else:
        random_list=random.sample(data,n)
    return random_list
print(weight_srs(data,3,weights,with_replacement=True))
