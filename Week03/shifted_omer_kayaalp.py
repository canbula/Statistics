def shifted(data):
    mean = sum(data) / len(data)
    s = sorted(data)  
    n = len(s)  
    median = (s[n//2] + s[(n-1)//2]) / 2 
    return abs((mean - median) / mean) * 100 
