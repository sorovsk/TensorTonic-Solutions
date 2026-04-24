import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code her
    y_pred, y_true = np.asarray(y_pred), np.asarray(y_true)
    n = y_pred.shape
    return np.mean((y_pred - y_true) ** 2)
