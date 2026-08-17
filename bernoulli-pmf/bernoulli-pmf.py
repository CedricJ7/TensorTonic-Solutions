import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = [1-p if x[i] == 0 else p for i in range(len(x))]
    mean = p
    var = p*(1-p)
    return np.array(pmf), mean, var