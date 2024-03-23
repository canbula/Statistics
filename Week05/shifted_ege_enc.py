def shifted(data):
    mean = sum(data) / len(data)
    
    n = len(data)
    sorted_data = sorted(data)
    median = (sorted_data[n//2] if n % 2 != 0 else (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2)
    
    p_diff = ((mean - median) / mean) * 100
    return p_diff


first_data = [10, 20, 30, 40, 50]  #Difference will be 0
second_data = [25,32.3,46,48] #Difference will not be 0 at this noisy data

first_result = shifted(first_data)
second_result = shifted(second_data)
print("Percentage diff:",first_result)
print("Percentage diff:",second_result)
