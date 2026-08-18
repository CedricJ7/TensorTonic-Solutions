import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Applique un inverted dropout à l'entrée x avec une probabilité d'extinction p.
    Retourne (output, dropout_pattern).
    """
    x = np.asarray(x)
    
    if p >= 1.0:
        return np.zeros_like(x), np.zeros_like(x, dtype=int)
    
    random_gen = np.random.default_rng(seed=rng)
    
   # 1. Le masque contient directement 2.0 et 0.0
    dropout_pattern = (random_gen.random(x.shape) > p) / (1 - p)

    # 2. La sortie utilise ce masque mis à l'échelle
    output = x * dropout_pattern
    
    return output, dropout_pattern
    
    
