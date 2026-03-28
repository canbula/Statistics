import numpy as np
def shifted(data):
    mean_val = np.mean(data)
    median_val = np.median(data)
    if mean_val == 0:
        return 0.0     
    percentage_diff = ((mean_val - median_val) / mean_val) * 100
    return percentage_diff
