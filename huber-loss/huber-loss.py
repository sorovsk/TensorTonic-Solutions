import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    e = y_true - y_pred
    a = np.abs(e)
    return np.mean(np.where(a > delta, delta * (a - delta / 2), e ** 2 / 2))