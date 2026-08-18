import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    pe = np.zeros((seq_len, d_model))
    
    pos = np.arange(seq_len).reshape(-1, 1)
    paire = np.arange(0, d_model, 2)
    
    angles = pos / (base ** (paire / d_model))
    
    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :d_model // 2])
    
    return pe