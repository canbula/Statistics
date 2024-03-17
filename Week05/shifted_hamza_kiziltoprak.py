import central_tendency as ct
def shifted(lst):
    mean = ct.mean(lst)
    median = ct.median(lst)
    result = abs((mean - median)/mean) * 100
    return result
