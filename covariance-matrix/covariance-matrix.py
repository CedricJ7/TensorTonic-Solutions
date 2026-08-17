import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    if len(X) < 2 or isinstance(X[0], (int, float)):
        return None
    X = np.asarray(X)
    X = X - np.mean(X, axis = 0)
    return 1/(len(X)-1)*X.T@X