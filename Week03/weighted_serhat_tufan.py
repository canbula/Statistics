import random
def weighted_srs(data,n,weights,with_replacement):
    if(with_replacement):
        return random.choices(population=data,weights=weights,k=n)
    else:
        return(random.sample(population=data,k=n))
#data=["Durhasan","Bakhele","Sövüşçü","Döndü"]
#weights=[0.1,0.6,0.1,0.2]
#sample=weighted_srs(data=data,n=3,weights=weights,with_replacement=True)
#print(sample)
