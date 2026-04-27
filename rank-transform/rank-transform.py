def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    idxs = [(val, i) for i, val in enumerate(values)]
    idxs.sort(key = lambda x: x[0])
    print (idxs)

    n = len(values)
    rk = 0
    ranks = [0.0] * n
    i = 0
    while i < n:
        rk += 1
        cnt = rk
        j = i + 1
        while j < n and idxs[j][0] == idxs[i][0]:
            rk += 1
            cnt += rk
            j += 1
            
        for k in range(i, j):
            ranks[idxs[k][1]] = cnt / (j - i)

        i = j
            
    print (ranks)
    
    return ranks

rank_transform([10, 30, 30, 30, 20])