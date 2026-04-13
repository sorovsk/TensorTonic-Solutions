import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    # step 0
    # 先将输入转换为NumPy数组，并指定高精度浮点类型
    x_arr = np.array(x, dtype=np.float64)
    p_arr = np.array(p, dtype=np.float64)
    
    # 验证概率和（使用更宽松的容差，如1e-6）
    if not np.allclose(np.sum(p_arr), 1.0, atol=1e-6):
        raise ValueError("probabilities must sum to 1")
    
    # 验证x和p形状匹配
    if x_arr.shape != p_arr.shape:
        raise ValueError("x and p must have the same shape")
    
    # 计算并返回期望值
    return np.sum(x_arr * p_arr)
