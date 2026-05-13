import numpy as np
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    n = len(X)
    d_in = len(X[0])
    d_out = len(W[0])
    
    # 初始化输出矩阵
    Y = [[0.0] * d_out for _ in range(n)]
    
    for i in range(n):
        for j in range(d_out):
            # 计算点积 X[i] 与 W 的第 j 列
            s = 0.0
            for k in range(d_in):
                s += X[i][k] * W[k][j]
            Y[i][j] = s + b[j]
            
    return Y