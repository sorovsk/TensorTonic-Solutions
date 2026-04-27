

def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    cnt = 0
    for rec, true in zip(recommendations, ground_truth):
        s1, s2 = set(rec[:k]), set(true)
        if s1 & s2:
            cnt += 1
    return cnt / len(recommendations)
        
    