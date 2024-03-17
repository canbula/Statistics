def shifted(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mean = sum(data) / n
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2 if n % 2 == 0 else sorted_data[n // 2]
    difference = ((mean - median) / mean) * 100
    return difference
data = [1, 2, 3, 4, 5]
result = shifted(data)
print("Percentage difference between mean and median:", result)
