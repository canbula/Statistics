def shifted(data):
    n = len(data)
    s = sorted(data)
    mean = sum(data) / n
    med = (s[n//2] + s[-(n//2 + 1)]) / 2
    return abs(mean - med) / abs(mean) * 100 if mean else 0
        
    