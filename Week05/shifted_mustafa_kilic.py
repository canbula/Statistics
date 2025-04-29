import statistics

def shifted(data):
    if not data:
        return None
    mean = statistics.mean(data)
    median = statistics.median(data)
    return 0 if median == 0 else abs(mean - median) / abs(mean) * 100
