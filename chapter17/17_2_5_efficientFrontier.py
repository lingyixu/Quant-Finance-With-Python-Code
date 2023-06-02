def plot_efficient_frontier(ret, cov_mat, N=5000):

    assert len(ret)==len(cov_mat), 'Please make sure the returns matches the shape of the covariance matrix.'

    # compute coefficients
    n = len(ret)
    a = np.ones(n).T@np.linalg.inv(cov_mat)@ret
    b = ret.T@np.linalg.inv(cov_mat)@ret
    c = np.ones(n).T@np.linalg.inv(cov_mat)@np.ones(n)
    d = b*c-a**2

    # compute optimal portfolios
    ret_arr = np.linspace(0.05,0.2,N)
    vol_arr = np.zeros(N)
    weight_arr = np.zeros((N, len(ret)))
    
    for i in range(N):
        w = 1/d*(c*np.linalg.inv(cov_mat)@ret-a*np.linalg.inv(cov_mat)@np.ones(n))*ret_arr[i] + 1/d*(b*np.linalg.inv(cov_mat)@np.ones(n)-a*np.linalg.inv(cov_mat)@ret)
        vol_arr[i] = np.sqrt(w.T@cov_mat@w)
        weight_arr[i,:] = w

    # plot the efficient frontier
    plt.scatter(vol_arr, ret_arr)
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.show()
    
    return weight_arr, ret_arr, vol_arr