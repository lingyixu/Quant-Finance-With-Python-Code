def sim_Vasicek(r0, kappa, theta, sigma, T,nper):
    rate_path = np.zeros(T*nper)
    rate_path[0] = r0
    
    dt = 1/nper
    for i in range(1,T*nper):
        dWt = np.random.normal(0,np.sqrt(1/nper))
        
        rate_path[i] = rate_path[i-1] + kappa*(theta - rate_path[i-1]) * dt + sigma * dWt
             
    return rate_path