def shifted(data):
    mean_value = mean(data)
    median_value = median(data)
    difference = ((mean_value - median_value) / median_value) * 100
    return difference
