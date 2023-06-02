def inverse_cov_mat(cov_mat, eps=1e-2, is_plot=True):
    
    w, v = np.linalg.eig(cov_mat)

    # step 1. check if eigenvalues are non-negative 
    assert np.where(w>=0, True, False).sum()==len(w), 'Please ensure the covariance matrix is positive semi-definite.'
    
    # step 2. calculate relative weights and drop small eigenvalues
    weighted_w = w/np.sum(w)
    if is_plot:
        plt.plot(np.sort(w)[::-1], marker='x', label='eigenvalue')
        plt.legend()
        plt.show()
        plt.bar(range(len(w)), np.sort(weighted_w)[::-1], width=0.3, label='relative weight')
        plt.legend()
        plt.show()
        
    w_hat = np.where(weighted_w>=eps, w, 0)
    noise_free_w = w_hat*(np.sum(w)/np.sum(w_hat))

    # step 3. calculate inverse matrix
    inv_mat = v@np.diag(np.where(noise_free_w!=0, 1/noise_free_w, 0))@v.T

    return w, noise_free_w, inv_mat