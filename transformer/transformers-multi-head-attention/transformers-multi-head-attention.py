import numpy as np

# 这是提供的 softmax 辅助函数，
# 用于将输入向量归一化为概率分布（和为1），
# 同时通过减去最大值来避免数值溢出。
def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    """
    # 获取输入形状
    batch, seq_len, d_model = Q.shape
    d_k = d_model // num_heads   # 每个头的维度
    
    # 1. 线性投影 Q, K, V
    Q_proj = Q @ W_q   # (batch, seq_len, d_model)
    K_proj = K @ W_k
    V_proj = V @ W_v
    
    # 2. 重塑为 (batch, seq_len, num_heads, d_k)
    
    Q_reshaped = Q_proj.reshape(batch, seq_len, num_heads, d_k)
    K_reshaped = K_proj.reshape(batch, seq_len, num_heads, d_k)
    V_reshaped = V_proj.reshape(batch, seq_len, num_heads, d_k)
    
    # 3. 转置为 (batch, num_heads, seq_len, d_k)
    # 相比于原来 seq_len 和 num_heads 对调
    Q_head = np.transpose(Q_reshaped, (0, 2, 1, 3))
    K_head = np.transpose(K_reshaped, (0, 2, 1, 3))
    V_head = np.transpose(V_reshaped, (0, 2, 1, 3))
    
    # 4. 计算缩放点积注意力分数
    scores = np.matmul(Q_head, K_head.transpose(0, 1, 3, 2)) / np.sqrt(d_k)
    # scores 形状: (batch, num_heads, seq_len, seq_len)
    
    # 5. 应用 softmax 得到注意力权重
    attention_weights = softmax(scores, axis=-1)
    
    # 6. 加权求和得到每个头的输出
    head_output = np.matmul(attention_weights, V_head)
    # head_output 形状: (batch, num_heads, seq_len, d_k)
    
    # 7. 转置并重塑为 (batch, seq_len, d_model)
    head_output = np.transpose(head_output, (0, 2, 1, 3))
    concat_output = head_output.reshape(batch, seq_len, d_model)
    
    # 8. 最终输出投影
    output = concat_output @ W_o
    
    return output