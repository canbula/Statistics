def shifted(data):
    mean = sum(data) / len(data)
    
    n = len(data)
    sorted_data = sorted(data)
    median = (sorted_data[n//2] if n % 2 != 0 else (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2)
    
    p_diff = abs((mean - median) / mean) * 100
    return p_diff
