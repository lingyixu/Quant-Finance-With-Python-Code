def plot_eff_cal(rf, ret, cov_mat, N=5000):

    assert len(ret)==len(cov_mat), 'Please make sure the returns matches the shape of the covariance matrix.'

    # compte coefficients
    n = len(ret)
    a = np.ones(n).T@np.linalg.inv(cov_mat)@ret
    b = ret.T@np.linalg.inv(cov_mat)@ret
    c = np.ones(n).T@np.linalg.inv(cov_mat)@np.ones(n)
    d = b*c-a**2

    # compute optimal portfolios
    weight_arr = np.zeros((N, n))
    ret_arr = np.linspace(0.05,0.15,N)
    vol_arr = np.zeros(N)
    sharpe_arr = np.zeros(N)

    for i in range(N):
        w = 1/d*(c*np.linalg.inv(cov_mat)@ret-a*np.linalg.inv(cov_mat)@np.ones(n))*ret_arr[i] + 1/d*(b*np.linalg.inv(cov_mat)@np.ones(n)-a*np.linalg.inv(cov_mat)@ret)
        weight_arr[i,:] = w
        vol_arr[i] = np.sqrt(w.T@cov_mat@w)
        sharpe_arr[i] = (ret_arr[i]-rf)/vol_arr[i]

    # compute the tangency portfolio
    tan_idx = sharpe_arr.argmax()
    tan_weight = weight_arr[tan_idx,:]
    tan_ret = ret_arr[tan_idx]
    tan_vol = vol_arr[tan_idx]

    # compute the Capital Allocation Line
    x_arr = []
    y_arr = []
    for x in np.linspace(0, vol_arr[-1], N):
        x_arr.append(x)
        slope = (tan_ret-rf)/tan_vol
        y = slope*x + rf
        y_arr.append(y)

    # plot the efficient frontier with CAL
    plt.figure(figsize=(15,5))
    plt.scatter(vol_arr, ret_arr, s=5)
    plt.scatter(tan_vol, tan_ret, s=50)
    plt.scatter(x_arr, y_arr, s=0.25)
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.show()

    return tan_weight, (tan_vol, tan_ret)