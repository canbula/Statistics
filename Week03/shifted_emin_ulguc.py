import statistics

def shifted(data):
    m = statistics.mean(data)
    return abs(m - statistics.median(data)) / abs(m) * 100 if m else 0
