def shifted(arr):
    arr = sorted(arr)
    n = len(arr)
    mean = sum(arr) / n
    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    
    diff = abs(mean - median) / mean * 100
    
    return diff
