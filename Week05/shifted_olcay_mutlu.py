def shifted(set):
    if(set.__len__() == 0):
        return None
    set.sort()
    xmax = max(median(set), mean(set))
    xmin = min(median(set), mean(set))
    percentage = (xmax - xmin) / xmax * 100
    return percentage
