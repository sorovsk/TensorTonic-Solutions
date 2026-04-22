import numpy as np

def wasserstein_critic_loss(r, f):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    r, f = np.asarray(r), np.asarray(f)
    return np.mean(f) - np.mean(r)