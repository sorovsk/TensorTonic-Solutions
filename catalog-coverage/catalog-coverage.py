def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    sub = set()
    for recs in recommendations:
        sub.update(recs)
    return len(sub) / n_items