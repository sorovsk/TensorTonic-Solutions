def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    m = min_votes
    C = global_mean
    result = []
    for R, v in items:
        denominator = v + m
        # 防止除以0的情况在本题不会出现，因为v>=0, m>0
        wr = (v * R + m * C) / denominator
        result.append(wr)
    return result