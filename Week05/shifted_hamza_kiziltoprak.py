def shifted(lst):
    lst.sort()
    n = len(lst)
    median = lst[n//2] if n % 2 else (lst[n//2 - 1] + lst[n//2]) / 2
    result = abs((sum(lst) / n - median) / (sum(lst) / n)) * 100
    return result
