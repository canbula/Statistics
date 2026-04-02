import statistics
def shifted(data):
    median = statistics.median(data)
    mean = statistics.mean(data)
    return abs(mean - median) / abs(mean) * 100 if mean != 0 else 0
