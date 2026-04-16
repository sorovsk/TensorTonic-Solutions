import numpy as np

def f1_micro(y_true, y_pred):
    """
    计算多分类问题的微平均F1分数
    
    参数:
    y_true: 真实标签数组
    y_pred: 预测标签数组
    
    返回:
    float: 微平均F1分数
    """
    # 转换为numpy数组
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # 获取所有类别
    classes = np.unique(np.concatenate([y_true, y_pred]))
    
    # 初始化统计量
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    # 遍历每个类别计算统计量
    for cls in classes:
        # 真正例：真实和预测都是该类
        tp = np.sum((y_true == cls) & (y_pred == cls))
        # 假正例：预测是该类但真实不是
        fp = np.sum((y_true != cls) & (y_pred == cls))
        # 假负例：真实是该类但预测不是
        fn = np.sum((y_true == cls) & (y_pred != cls))
        
        total_tp += tp
        total_fp += fp
        total_fn += fn
    
    # 计算微平均精确率和召回率
    micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    
    # 计算微平均F1分数
    if micro_precision + micro_recall > 0:
        f1_micro_score = 2 * micro_precision * micro_recall / (micro_precision + micro_recall)
    else:
        f1_micro_score = 0.0
    
    return f1_micro_score
