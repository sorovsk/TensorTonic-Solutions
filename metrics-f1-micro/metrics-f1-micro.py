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

    # 使用numpy的比较操作，返回布尔数组
    equal_mask = y_true == y_pred
    
    # 统计True的个数，即相同元素的个数
    count = np.sum(equal_mask)

    return count / len(y_true)
    
    
