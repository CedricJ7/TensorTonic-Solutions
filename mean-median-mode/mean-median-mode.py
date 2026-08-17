import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    counts = Counter(x)
    max_freq = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_freq]
    
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    mode_val = float(min(modes))
    
    return mean_val, median_val, mode_val