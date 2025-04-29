def shifted(data):
    n = len(data)
    mean = int(sum(data) / n)
    if n % 2 == 1:
        median = data[int(n + 1 / 2 - 1)]
    median = int(data[int((n / 2) - 1)] + data[int(n / 2)] / 2)
    if mean == 0:
        return 0
    result = int(abs((mean - median) / mean) * 100)
    return result
