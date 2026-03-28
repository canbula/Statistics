def shifted(data):
    mean = sum(data) / len(data)  #calculates average (mean)
    s = sorted(data)  #sortes from small to large
    n = len(s)  #stores the total count
    median = (s[n//2] + s[(n-1)//2]) / 2  #calculates the median
    return abs((mean - median) / mean) * 100  #ensures the result is always positive for %
