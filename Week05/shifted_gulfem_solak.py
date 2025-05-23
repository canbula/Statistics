def shifted(numbers):
    if not numbers:
        return 0

    mean_val = sum(numbers) / len(numbers)

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)

    if n % 2 == 0:
        median_val = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median_val = sorted_nums[n // 2]

    if median_val == 0:
        return 0

    percentage_difference = ((mean_val - median_val) / abs(median_val)) * 100
    return percentage_difference
