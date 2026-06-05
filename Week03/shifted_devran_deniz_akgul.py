from statistics import mean, median

def shifted(sample):
    m = mean(sample)
    return abs(m - median(sample)) / abs(m) * 100
