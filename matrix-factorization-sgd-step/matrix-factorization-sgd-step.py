def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    U, V = np.asarray(U), np.asarray(V)
    e = r - sum(U * V)
    U_t = U + lr * (e * V - reg * U)
    V_t = V + lr * (e * U - reg * V)

    return U_t, V_t