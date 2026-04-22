import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    def cb(k):
        return comb(n, k) * (p ** k) * (1 - p) ** (n - k)
    # Write code here
    return cb(k), sum([cb(i) for i in range(k + 1)])
    