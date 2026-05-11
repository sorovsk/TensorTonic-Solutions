def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    def diff(arr):
        ret = []
        for i in range(1, len(arr)):
            ret.append(arr[i] - arr[i - 1])
        return ret
    for i in range(order):
        series = diff(series)
    return series