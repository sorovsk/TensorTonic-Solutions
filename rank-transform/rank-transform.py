def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    n = len(values)
    # Pair each value with its original index
    indexed = [(val, i) for i, val in enumerate(values)]
    # Sort by value
    indexed.sort(key=lambda x: x[0])

    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        # Find all indices with the same value
        while j + 1 < n and indexed[j + 1][0] == indexed[i][0]:
            j += 1
        # For positions i..j (0-based in sorted order),
        # 1-based ranks are (i+1) to (j+1)
        avg_rank = ( (i + 1) + (j + 1) ) / 2.0
        for k in range(i, j + 1):
            _, orig_idx = indexed[k]
            ranks[orig_idx] = avg_rank
        i = j + 1

    return ranks