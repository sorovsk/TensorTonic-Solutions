import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    mu = np.mean(x)
    # unbias
    var = sum((x - mu) ** 2) / (len(x) - 1)
    return var, np.sqrt(var)