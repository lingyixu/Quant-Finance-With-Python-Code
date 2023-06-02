def covMatShrinkage(cov_mat, vols, const_corr, phi):
    N = cov_mat.shape[0]
    
    #make the constant correlation covariance matrix with the proper vols
    const_corr_mat = np.full((N, N), const_corr)
    np.fill_diagonal(const_corr_mat, 1.0)

    vols_mat = np.diag(vols)
    const_cov_mat = vols_mat.T @ const_corr_mat @ vols_mat
    
    #combine the empirical and constant correlation covariance matrix
    cov_mat_hat = (1 - phi)* cov_mat + phi * const_cov_mat
    
    return cov_mat_hat