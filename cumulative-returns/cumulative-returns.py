def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    cur = 1.0
    ret = [0.0] * len(returns)
    for i, rate in enumerate(returns):
        cur *= 1 + rate
        ret[i] = cur - 1

    return ret
        