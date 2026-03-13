import random

def weighted_srs(data, n, weights, with_replacement):
    # If sampling with replacement directly use random.choices
    if with_replacement:
        return random.choices(data, weights=weights, k=n)

    #copy  lists so original data is not modified
    sample, d, w = [], data[:], weights[:]

    #select n elements based on their weights
    for _ in range(n):
        x = random.choices(d, weights=w, k=1)[0]  #pick one element
        i = d.index(x)                            # find its index
        sample.append(x)                          #add to sample
        d.pop(i); w.pop(i)                        #remove to avoid reselection

    return sample
