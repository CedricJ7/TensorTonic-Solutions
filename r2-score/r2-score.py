import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """Return the coefficient of determination."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float( 1 - np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2)) if len(set(y_true)) != 1 else float(1) if  np.array_equal(y_true, y_pred) else float(0)