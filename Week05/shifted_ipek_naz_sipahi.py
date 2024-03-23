def shifted(first):
    mean = sum(first) / len(first)
    n = len(first)
    if n % 2 == 0:
        median = (sorted(first)[n//2 - 1] + sorted(first)[n//2]) / 2
    else:
        median = sorted(first)[n//2]
    result = abs(((mean - median) / mean) * 100)
    return result
