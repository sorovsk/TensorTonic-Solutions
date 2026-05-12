def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    ret = []
    n, w = len(values), len(weights)
    d = sum(weights)
    for i in range(n - w + 1):
        window = values[i : i + w]
        ret.append(sum([x * y for x, y in zip(window, weights)]) / d)
    return ret