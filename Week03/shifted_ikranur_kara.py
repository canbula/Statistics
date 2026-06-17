def shifted(sample):
    mean = sum(sample) / len(sample)
    s = sorted(sample)
    n = len(s)
    median = s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2
    return 0 if mean == 0 else abs(mean-median)/abs(mean)*100
