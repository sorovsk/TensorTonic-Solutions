import numpy as np

def entropy_node(y):
    """
    计算一个节点的信息熵。

    参数:
    y : array-like
        包含节点中样本类别标签的一维数组。

    返回:
    float
        该节点的信息熵。
    """
    # 将输入转换为NumPy数组
    y = np.asarray(y)
    
    # 如果节点为空，熵为0
    if y.size == 0:
        return 0.0
    
    # 获取唯一类别及其计数
    unique_labels, counts = np.unique(y, return_counts=True)
    
    # 计算每个类别的概率
    probabilities = counts / y.size
    
    # 计算信息熵
    # 使用 np.log2 并添加一个极小值以避免对0取对数
    entropy_value = -np.sum(probabilities * np.log2(probabilities + np.finfo(float).eps))
    
    # 确保熵非负（处理浮点误差）
    return max(0.0, entropy_value)
