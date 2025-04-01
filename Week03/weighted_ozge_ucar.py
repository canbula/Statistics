import random
def weight_srs(data , n,weights, with_replacement = False):
    if with_replacement == True or weights != None:
        random_list= random.choices(data , m=n, weights=weights) #i prefer choices method because of sample took just two variable
    else:
        random_list=random.sample(data,n)
    return random_list
