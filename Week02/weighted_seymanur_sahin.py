import random
def weighted_srs(data, n, weights, *, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n) # Sample with replacement
    result, temp_data, temp_weights = [], list(data), list(weights) # Create temporary lists
    for _ in range(n): # Repeat until n items are selected
        chosen_item = random.choices(temp_data, weights=temp_weights, k=1)[0] # Select one item
        target_index = temp_data.index(chosen_item) # Find the index of the selected item
        result.append(temp_data.pop(target_index)) # Move item to result and remove from data
        temp_weights.pop(target_index) # Remove the weight to match the updated data
    return result # Return the final list
