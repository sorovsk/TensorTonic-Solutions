import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    t = np.exp(x)
    return (t - 1/t) / (t + 1/t)