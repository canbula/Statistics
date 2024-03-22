def shifted(lst):
    mean = sum(lst) / len(lst)
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        median = sorted_list[mid]
    return abs((mean - median) / median) * 100
