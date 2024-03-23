def shifted(lst):
    mean = sum(lst) / len(lst)
    mid = len(sorted(lst)) // 2
    if len(sorted(lst)) % 2 == 0:
        median = (sorted(lst)[mid - 1] + sorted(lst)[mid]) / 2
    else:
        median = sorted(lst)[mid]
    return abs((mean - median) / mean) * 100
