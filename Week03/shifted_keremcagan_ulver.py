def shifted(sample):
    n = len(sample)
    mean = sum(sample) / n
    if not mean:
        return 0
    sorted_sample = sorted(sample)
    median = (sorted_sample[n // 2] + sorted_sample[-(n // 2 + 1)]) / 2
    return abs(mean - median) / abs(mean) * 100
