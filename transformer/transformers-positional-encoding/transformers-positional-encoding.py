import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # 确保 d_model 是偶数（题目保证，但可作断言）
    assert d_model % 2 == 0, "d_model must be even"
    
    # 1. 创建位置向量 (seq_length, 1)
    pos = np.arange(seq_length).reshape(-1, 1)  # (seq_length, 1)
    
    # 2. 计算频率项的倒数（避免大指数幂）
    # 公式: div_term[i] = 1 / (10000^(2i/d_model)) = exp(- (2i/d_model) * ln(10000))
    i = np.arange(0, d_model, 2)  # 偶数索引对的序号 (0,2,4,...)
    div_term = np.exp(i * (-np.log(10000.0) / d_model))  # 长度 d_model//2
    
    # 3. 计算角度: pos * div_term，广播后形状 (seq_length, d_model//2)
    angle = pos * div_term  # (seq_length, d_model//2)
    print(angle)
    # 4. 初始化编码矩阵
    pe = np.zeros((seq_length, d_model), dtype=np.float64)
    print(pe)
    # 5. 填充 sin 到偶数索引 (0,2,4,...)，cos 到奇数索引 (1,3,5,...)
    pe[:, 0::2] = np.sin(angle)
    pe[:, 1::2] = np.cos(angle)
    
    return pe

positional_encoding(4, 6)