import random
def weight_srs(data , n,weights, with_replacement = False):#i create a function which named weight_srs take 4 parameter
    if with_replacement == True or weights != None:
        random_list= random.choices(data , k=n, weights=weights)#random_list variable hold a random choices from data set with weights
    else:
        random_list=random.sample(data,n)#if there is no weights then random_list variable hold just random elenments of data set
    return random_list#the function weight_srs return the random_list
print(weight_srs(data,3,weights,with_replacement=True))#i called the function in a print operation
