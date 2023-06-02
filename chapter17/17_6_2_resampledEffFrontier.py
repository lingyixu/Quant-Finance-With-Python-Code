def resampled_efficient_frontier(ret, cov_mat, size=252, N_path=1000, N_point=5000):
    
    assert len(ret)==len(cov_mat), 'Please make sure the returns matches the shape of the covariance matrix.'
    n = len(ret)
    ret_arr = np.linspace(0,0.3,N_point)
    vol_arr = np.zeros(N_point)
    weight_arr_all = np.zeros((N_path,N_point,n))

    for i in range(N_path):
        
        # generate resampled paths
        data = np.random.multivariate_normal(ret, cov_mat, size=size)
        ret_i = data.mean(axis=0)
        cov_mat_i = np.cov(data.T)

        weight_arr = np.zeros((N_point,n))
        a = np.ones(n).T@np.linalg.inv(cov_mat_i)@ret_i
        b = ret_i.T@np.linalg.inv(cov_mat_i)@ret_i
        c = np.ones(n).T@np.linalg.inv(cov_mat_i)@np.ones(n)
        d = b*c-a**2

        # compute the efficient frontier
        for j in range(N_point):
            w = 1/d*(c*np.linalg.inv(cov_mat_i)@ret_i-a*np.linalg.inv(cov_mat_i)@np.ones(n))*ret_arr[j] + 1/d*(b*np.linalg.inv(cov_mat_i)@np.ones(n)-a*np.linalg.inv(cov_mat_i)@ret_i)
            weight_arr[j,:] = w

        weight_arr_all[i,:] = weight_arr

    # average the weights of multiple efficient frontiers
    avg_weight_arr = weight_arr_all.mean(axis=0)
    
    for k in range(N_point):
        w = avg_weight_arr[k,:]
        vol_arr[k] = np.sqrt(w.T@cov_mat@w)

    return ret_arr, vol_arr