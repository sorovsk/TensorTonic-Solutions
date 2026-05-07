import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)
    norm = np.sqrt(np.sum(v**2, axis=-1, keepdims= True))
    return np.where(norm > 0, v / norm, 0.0)
