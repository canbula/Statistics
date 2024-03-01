import random
def weighted_srs(population,n,weights,with_replacement=False):
    if with_replacament:
        resultsList = random.choices(population, weights=weights, k=n)
        return  resultsList
    else:
        indexOfSample=random.sample(range(len(population)),n)
        resultsList=[population[i]for i in indexOfSample]
        return resultsList
