def shifted(data):
    if(data.__len__() == 0):
        return None
    data.sort()
    xmax = max(median(data), mean(data))
    xmin = min(median(data), mean(data))
    percentage = (xmax - xmin) / xmax * 100
    return percentage
