import statistics

def shifted(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    return abs(mean - median) / abs(mean) * 100 if mean != 0 else 0
