def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    dict = {}
    for i, v in enumerate(ordering):
        dict[v] = i
    ret = [0] * len(values)
    for i, o in enumerate(values):
        ret[i] = dict[o]
    return ret