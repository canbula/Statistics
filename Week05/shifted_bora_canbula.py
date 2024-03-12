def shifted(data):
    mean = sum(data) / len(data)
    data = sorted(data)
    n = len(data)
    median = data[int((n + 1) / 2) - 1] if n % 2 == 1 else (data[(n // 2) - 1] + data[((n // 2) + 1) - 1]) / 2
    return abs(mean - median) / abs(mean) * 100
