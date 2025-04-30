def shifted(data):
    data = [abs(value) for value in data]
    n = len(data)
    mean = sum(data) / n
    if n % 2 == 1:
        median = data[int((n + 1) / 2 - 1)]
    else:
        median = data[int((n / 2) - 1)] + data[int(n / 2)] / 2
    return int(abs((mean - median) / mean) * 100) 
