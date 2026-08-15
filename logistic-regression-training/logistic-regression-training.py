import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64).ravel()
    
    n_samples, n_features = X.shape
    
    # Initialisation : w vecteur 1D de taille (n_features,), b scalaire
    w = np.zeros(n_features)
    b = 0.0
    
    for _ in range(steps):
        # Prédiction des probabilités : shape (n_samples,)
        linear_model = X @ w + b
        p = _sigmoid(linear_model)
        
        # Gradients
        error = p - y
        grad_w = (1 / n_samples) * (X.T @ error)
        grad_b = (1 / n_samples) * np.sum(error)
        
        # Mise à jour des paramètres
        w -= lr * grad_w
        b -= lr * grad_b
        
    return w, b