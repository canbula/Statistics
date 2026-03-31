def shifted(data):
    s = sorted(data)  # sort values for median calculation
    n = len(s)
    mean = sum(s) / n
    median = (s[n//2] + s[(n-1)//2]) / 2  # works for even & odd lengths
    shift = abs(mean - median) / abs(mean) * 100 if mean else 0
    return min(shift, 100)  # limit extreme values
