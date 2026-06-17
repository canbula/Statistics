def shifted(data):
    n = len(data)
    s = sorted(data)
    mean = sum(data) / n
    median = (s[n//2 - 1] + s[n//2]) / 2 if n % 2 == 0 else s[n//2]
    return abs(mean - median) / abs(mean) * 100 if mean else 0
