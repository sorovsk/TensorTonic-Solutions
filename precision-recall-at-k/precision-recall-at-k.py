import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended, relevant = np.array(recommended), np.array(relevant)
    # Write code here
    # 确保 k 不超过推荐列表长度
    k = min(k, len(recommended))
    
    # 获取前 k 个推荐项
    recommended_at_k = recommended[:k]
    
    # 计算命中数：前 k 个推荐中属于相关项的数量
    hit_count = len(set(recommended_at_k) & set(relevant))
    
    # 计算 Precision@k
    precision = hit_count / k if k > 0 else 0.0
    
    # 计算 Recall@k
    total_relevant = len(set(relevant))
    recall = hit_count / total_relevant if total_relevant > 0 else 0.0
    
    return [precision, recall]