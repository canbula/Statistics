import random
def weighted_srs(data, n, weights, with_replacement):
    weighted_data = [] # Weighted list of data
    a = 0
    for x in data:
        b = 0
        while b < weights[a]:
            weighted_data.append(x) # Adds the data weight times into the weighted list
            b+=1
        a+=1
    if with_replacement:
        return random.choices(weighted_data, k = n)
    else:
        return random.sample(weighted_data , k = n)
