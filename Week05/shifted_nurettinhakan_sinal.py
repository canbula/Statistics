def shifted(data):
    if len(data) == 0:
        return 0
    mean = sum(sorted(data)) / len(sorted(data))
    median = (sorted(data)[len(sorted(data)) // 2 - 1] + sorted(data)[len(sorted(data)) // 2]) / 2 if len(sorted(data)) % 2 == 0 else sorted(data)[len(sorted(data)) // 2]
    result = abs((mean - median) / mean) * 100
    return result
