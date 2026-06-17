from statistics import mean, median

def shifted(sample):
    avg = mean(sample)
    med = median(sample)

    return 0 if avg == 0 else abs(med - avg) / abs(avg) * 100