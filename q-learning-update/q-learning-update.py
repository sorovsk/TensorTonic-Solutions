import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    # pass
    Q_new = np.array(Q, dtype = float)
    update = r + gamma * np.max(Q_new[s_next]) - Q_new[s, a]
    Q_new[s, a] += alpha * update
    return Q_new