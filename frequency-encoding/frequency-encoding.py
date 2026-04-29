from collections import Counter

def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    c = Counter(values)
    n = len(values)
    ret = [0] * n
    for i, v in enumerate(values):
        ret[i] = c[v] / n
    return ret