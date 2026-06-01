import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    # x = np.asarray(x)
    arr = np.atleast_1d(np.asarray(x, dtype=float))
    
    # SELU 公式
    out = np.where(arr > 0, lam * arr, lam * alpha * (np.exp(arr) - 1))
    
    # 四舍五入到 4 位小数，转为列表返回
    return np.round(out, 4).tolist()
