import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X)
    min = np.min(X, axis = axis, keepdims = True)
    max = np.max(X, axis = axis, keepdims = True)
    diff = max - min
    diff = np.where(diff < eps, 1.0, diff)
    return (X - min) / diff