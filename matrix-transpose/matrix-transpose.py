import numpy as np
    
def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    R = A.shape[0]
    C = A.shape[1]
    res = np.empty([C,R])
    # or use np.zeros([m,n])
    for i in range(0,R):
        for j in range(0,C):
            res[j,i] = A[i,j]
    return(res)
