def shifted(data):

    n = len(data)
    sorted_data = sorted(data)
    
   
    mean = sum(data) / n
    
    
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    difference = abs(mean - median)
    percentage = (difference / mean) * 100
    
    return percentage

data = [10, 20, 30, 40, 50]
shifted_percentage = shifted(data)
print("Percentage difference between mean and median:", shifted_percentage)
