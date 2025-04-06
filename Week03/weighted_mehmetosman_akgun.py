import random

def weighted_srs(data, n, weights, with_replacement=False):
    sampled = []  # List to hold selected samples
    while len(sampled) < n:
        choice = random.choices(data, weights=weights)[0]  # Randomly select a sample based on weights.
        if with_replacement or choice not in sampled: # If not sampling with replacement or the chosen sample is not already in the samples list:
            sampled.append(choice)  # Add the chosen sample to the samples list.
    return sampled  # Return the list of selected samples

