def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    ret = []
    for val in values:
        ret.append([val ** p for p in range(degree + 1)])
    return ret