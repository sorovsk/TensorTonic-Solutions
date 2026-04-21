import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    ssr = np.sum((y_true - y_pred) ** 2)
    mean = np.mean(y_true)
    sst = np.sum((y_true - mean) ** 2)

    # 处理常值目标变量的边界情况 (ss_tot == 0)
    if sst < 1e-12:
        # 如果真实值全部相同
        if ssr < 1e-12:
            # 预测值也完全匹配（即预测值也等于该常数），完美拟合
            return 1.0
        else:
            # 预测值不匹配，模型无法解释任何变异（因为无变异），视为无效或0
            return 0.0
            
    # 标准 R² 计算公式
    return 1.0 - (ssr / sst)
    