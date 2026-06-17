def shifted(data):
    n = len(data)
    mean = sum(data) / n
    s = sorted(data)
    median = (s[n//2] + s[~n//2]) / 2
    return abs(mean - median) / abs(mean) * 100
