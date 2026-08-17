import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x, y = np.asarray(x), np.asarray(y)
    return(int(np.sum(np.abs(x-y))))