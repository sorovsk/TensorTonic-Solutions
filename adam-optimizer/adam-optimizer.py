import numpy as np

def adam_step(param, grad, m, v, t, alpha=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    # step0
    param = np.array(param, dtype=np.float64)
    grad = np.array(grad, dtype=np.float64)
    m = np.array(m, dtype=np.float64)
    v = np.array(v, dtype=np.float64)
    
    # step1
    m_t = beta1 * m + (1 - beta1) * grad
    # step2
    v_t = beta2 * v + (1 - beta2) * grad ** 2
    # step3
    m_hat = m_t / (1 - beta1 ** t)
    v_hat = v_t / (1 - beta2 ** t)
    # step4
    param_t = param - alpha * m_hat / (np.sqrt(v_hat) + eps)

    return (param_t, m_t, v_t)