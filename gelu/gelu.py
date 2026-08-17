import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    erf = np.vectorize(math.erf)
    return(1/2*np.asarray(x)*(1+erf(x/np.sqrt(2))))

