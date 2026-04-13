import numpy as np

def precision_recall_at_k(rec, rel, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # recommended, relevant = np.array(recommended), np.array(relevant)
    # constrain
    k = min(k, len(rec))
    rel = set(rel)
    
    # intersection
    hit = len(set(rec[:k]) & rel)
    
    # 计算 Precision@k
    prec = hit / k if k > 0 else 0.0
    
    # 计算 Recall@k
    rel = len(rel)
    recall = hit / rel if rel > 0 else 0.0
    
    return [prec, recall]