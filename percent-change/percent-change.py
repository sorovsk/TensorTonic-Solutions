def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    n = len(series)
    ret = [0.0] * (n - 1)
    for i in range(1, n):
        pre, cur = series[i - 1], series[i]
        ret[i - 1] = 0 if pre == 0 else (cur - pre) / pre 
    return ret
        