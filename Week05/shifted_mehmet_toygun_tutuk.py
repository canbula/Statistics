def shifted(data):
    mean_value = sum(data) / len(data)
    sorted_data = sorted(data)
    median_value = sorted_data[len(sorted_data) // 2] if len(data) % 2 != 0 else (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2
    return abs(mean_value - median_value) / mean_value * 100
