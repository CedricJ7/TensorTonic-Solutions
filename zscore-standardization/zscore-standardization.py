import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """Return population Z-scores along axis."""
        
    X = np.asarray(X)
    µ = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis = axis, keepdims=True)
    return (X - µ) / np.where(std > eps, std, 1.0)