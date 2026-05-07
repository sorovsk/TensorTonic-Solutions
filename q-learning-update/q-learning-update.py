import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    # pass
    Q_new = np.array(Q, dtype=float)
    
    # TD target = r + γ * max_a' Q(s_next, a')
    td_target = r + gamma * np.max(Q_new[s_next])
    
    # TD error = target - Q(s, a)
    td_error = td_target - Q_new[s, a]
    
    # 更新 Q(s, a)
    Q_new[s, a] += alpha * td_error

    return Q_new