import random

data=["Zeynep","Nur","Ali","Ahmet","Fatma","Sude","Ece","Sevde"]
weights=[10,20,30,40,50,60,70,80]

def weighted_srs(data,n,weights,with_replacement):
    if(with_replacement==True):
        return random.sample(data,n)
    else:
        return random.choice(data,weights,n)

sample = weighted_srs(data,4,20,True)
print(sample)
