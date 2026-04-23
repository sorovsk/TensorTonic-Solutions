def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    map = {}
    for s in sentences:
        for w in s:
            if w in map:
                map[w] += 1
            else:
                map[w] = 1
    return map