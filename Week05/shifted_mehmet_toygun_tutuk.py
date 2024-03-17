def shifted(data):
    mean_value = mean(data)
    median_value = median(data)
    return abs(mean_value - median_value) / mean_value * 100
