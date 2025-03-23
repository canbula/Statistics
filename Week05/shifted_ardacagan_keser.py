def shifted(list):
    list.sort()
    mean = sum(list) / len(list)
    
    if len(list) % 2 == 0:
        median = (list[(len(list) // 2) - 1] + list[(len(list) // 2) + 1 - 1]) / 2
    else:
        median = list[((len(list) + 1) // 2) - 1]
        
    return abs((mean - median) / mean) * 100
