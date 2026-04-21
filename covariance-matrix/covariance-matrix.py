import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim != 2:
        return None
    n, d = X.shape
    if n < 2:
        return None
    mean = np.mean(X, axis = 0)
    center = X - mean
    
    return center.T @ center / (n - 1)