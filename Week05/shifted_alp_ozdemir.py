def shifted(data):
    data = [abs(value) for value in data]
    n = len(data)
    mean = int(sum(data) / n)
    if n % 2 == 1:
        median = data[int(n + 1 / 2 - 1)]
    median = int(data[int((n / 2) - 1)] + data[int(n / 2)] / 2)
    result = int(abs((mean - median) / mean) * 100)
    return result
