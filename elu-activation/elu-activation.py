import numpy as np 

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    arr = np.asarray(x, dtype=float)
    out = np.where(arr >= 0, arr, alpha * (np.exp(arr) - 1))
    # 四舍五入到 4 位小数，与 SELU 示例风格保持一致
    return np.round(out, 4).tolist()