def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    unrated = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    
    # Sort by score descending
    unrated.sort(key = lambda x : x[0], reverse = True)

    print (unrated)
    
    # Return indices of the top k (or all if fewer are available)
    return [i for _, i in unrated[:k]]

top_k_recommendations([3.5,1.2,4.8,2.1,5], [0, 2], 2)