# cholesky
mat = np.random.rand(5, 5) # full-rank square matrix
A = mat @ mat.T  # matrix product to get positive definite matrix
L = cholesky(A)  # lower triangular matrix

# eigenvalue decomposition
mat = np.vstack([np.random.rand(4, 5), np.zeros(5)]) # rank-deficient square matrix
A = mat @ mat.T  # matrix product to get positive-semidefinite matrix
w, v = eig(A)  # eigenvalues w and normalized eigenvectors v