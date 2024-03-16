def shifted(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mean = sum(data) / n
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2] 
    difference = ((mean - median) / mean) * 100
    return difference
