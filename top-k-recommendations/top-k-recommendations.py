def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    unrated = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    
    # Sort by score descending
    unrated.sort(key=lambda x: x[0], reverse=True)
    
    # Return indices of the top k (or all if fewer are available)
    return [idx for _, idx in unrated[:k]]