import random
def simple_random_sampling(data, n, weights, with_replacement):
    if len(weights) != len(data):
        sampled_data = random.choices(weights, k=n)
    else:
        sampled_data = random.sample(weights, n)
    return sampled_data
sampled_data = simple_random_sampling([1,2,3,4,5,6,7,8,9,10], 5, [52,68,79,45,71,92,64,47,57,84], True)
print("Sampled Data : {}".format(sampled_data))
    
