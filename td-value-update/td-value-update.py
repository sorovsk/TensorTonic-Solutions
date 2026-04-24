import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    V_new = V.copy()                       # 不修改原数组
    td_error = r + gamma * V[s_next] - V[s] # 计算 TD 误差
    V_new[s] = V[s] + alpha * td_error     # 更新状态 s 的值
    return V_new
