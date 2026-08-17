import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts = True)
    p = counts/ len(y)
    p = p[p>0]
    return float(-np.sum(p*np.log2(p)))