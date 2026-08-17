import numpy as np

def pca_projection(X, k):
    """Projette les données sur les k composantes principales."""
    X = np.asarray(X, dtype=float)
    
    # 1. Centrage des données 📏
    X_centered = X - np.mean(X, axis=0, keepdims=True)
    
    # 2. Matrice de covariance 📊
    n = X.shape[0]
    C = (1 / (n - 1)) * (X_centered.T @ X_centered)
    
    # 3. Décomposition spectrale ⚖️
    eigenvalues, eigenvectors = np.linalg.eigh(C)
    
    # 4. Sélection des k meilleurs vecteurs (ordre décroissant) 🧭
    indices_top_k = np.argsort(eigenvalues)[::-1][:k]
    W = eigenvectors[:, indices_top_k]
    
    # 5. Projection ✖️
    X_proj = X_centered @ W
    
    return X_proj