def shifted(data):
    sorted_data = data.sort()
    n = len(data)
    mean = sum(data) / n
    median = data[n//2] if n % 2 == 0 else (data[n//2 - 1] + data[n//2]) / 2
    return abs((mean - median)/median)*100
