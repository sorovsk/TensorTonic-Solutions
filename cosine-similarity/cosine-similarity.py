import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a, b = np.asarray(a), np.asarray(b)
    dot = a.dot(b)
    na, nb = np.linalg.norm(a), np.linalg.norm(b)

    if na == 0 or nb == 0:
        return 0.0
    return float(dot / (na * nb))