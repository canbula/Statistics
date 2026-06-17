import statistics
def shifted(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std = statistics.stdev(data)
    return abs(3 * (mean - median) / std)
