import statistics as s
def shifted(smple):
    diff = abs(s.mean(smple) - s.median(smple))
    n = len(smple)
    shift = (diff / abs(s.mean(smple))) * 100
    return shift
