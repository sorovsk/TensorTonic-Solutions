import numpy as np

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code he
    values = np.asarray(values)
    
    theta = 2 * np.pi * values / period
    sin = np.sin(theta)
    cos = np.cos(theta)
    
    # 将 sin 和 cos 沿最后一个轴堆叠，保持输入形状
    return np.stack([sin, cos], axis=-1).tolist()
        