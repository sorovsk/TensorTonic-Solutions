def moving_median(values, w):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values)
    ret = []
    for i in range(n - w + 1):
        window = sorted(values[i : i + w])
        if w % 2 == 0:
            ret.append((window[w // 2] + window[w // 2 - 1]) / 2)
        else:
            ret.append(window[w // 2])
    return ret