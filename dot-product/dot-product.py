import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # x, y = np.asarray(x), np.asarray(y)
    # return(np.sum([x[i]*y[i] for i in range(len(x))]))
    # return(np.sum(x*y))
    return(np.dot(x,y))
    