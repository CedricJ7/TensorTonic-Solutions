import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    var = (1/(len(x)-1)*np.sum([(x[i] - np.mean(x))**2 for i in range(len(x))]))
    std_dev = np.sqrt(var) 
    return var, std_dev
    