import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    cnts = Counter(x)
    mode = min([num for num, cnt in cnts.items() if cnt == max(cnts.values())])
    return np.mean(x), np.median(x), mode