def shifted(data):
    data.sort()
    n = len(data)
    mean = sum(data) / n
    median = (data[n // 2] + data[n // 2 + 1]) / 2 if n % 2 == 0 else data[n // 2]
    return mean - median
