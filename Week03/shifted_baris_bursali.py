def shifted(sample):
    n = len(sample)
    mean = sum(sample) / n
    median = sorted(sample)[n // 2] if n % 2 != 0 else (sorted(sample)[n // 2 - 1] + sorted(sample)[n // 2]) / 2
    return abs(mean - median) / abs(mean) * 100