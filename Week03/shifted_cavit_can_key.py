def shifted(sample):
    data = sorted(sample)
    n = len(data)
    mean = sum(data) / n
    median = (data[(n - 1) // 2] + data[n // 2]) / 2
    return abs(mean - median) / abs(mean) * 100 if mean else 0
