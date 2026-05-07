import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    cnt = Counter(tokens)
    ret = np.zeros(len(vocab),  dtype=int)
    for i, v in enumerate(vocab):
        ret[i] = cnt[v]
    return ret   
    
    
    