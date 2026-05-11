from collections import Counter

def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    cnt = Counter(categories)
    n = len(targets)
    mp = {}
    
    for i in range(n):
        cate, val = categories[i], targets[i]
        if cate in mp:
            mp[cate] += val
        else:
            mp[cate] = val

    ret = [0] * n        
    for i, cate in enumerate(categories):
        ret[i] = mp[cate] / cnt[cate]
    return ret
        
        