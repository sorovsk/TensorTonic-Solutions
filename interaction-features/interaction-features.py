def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    rets = []
    for x in X:
        ret = x
        n = len(x)
        for i in range(n):
            for j in range(i + 1, n):
                ret.append(x[i] * x[j])
        rets.append(ret)
    return rets