def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a, b = set(set_a), set(set_b)
    if len(a) == 0 and len(b) == 0:
        return 0.0
    return len(a & b) / len(a | b)