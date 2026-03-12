import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    result, temp_data, temp_weights = [], list(data), list(weights) # create temporary lists
    for _ in range(n): # repeat until n items are selected
        chosen_item = random.choices(temp_data, weights=temp_weights, k=1)[0] # select one item
        target_index = temp_data.index(chosen_item) # find the index of the selected item
        result.append(temp_data.pop(target_index)) # move item to result and remove from data
        temp_weights.pop(target_index) # remove the weight to match the updated data
    return result
