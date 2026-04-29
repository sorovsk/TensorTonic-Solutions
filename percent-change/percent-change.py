def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    n = len(series)
    ret = [0.0] * (n - 1)
    for i in range(1, n):
        if series[i - 1] == 0:
            ret[i - 1] = 0
        else:
            ret[i - 1] = (series[i] - series[i - 1]) / series[i - 1]
    return ret
        