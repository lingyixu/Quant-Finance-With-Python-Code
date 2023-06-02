def var_gamma(sigma, v, theta, S0, T, r, q, n, N):
    
    dt = T/N
    w = np.log(1-theta*v-0.5*v*sigma**2)/v
    price_vec = np.empty(n)
    
    for i in range(n):
        
        lns0 = np.log(S0)
        xt = 0
        
        for j in range(N):
            
            gamma = np.random.gamma(dt/v, v)
            z = np.random.normal(0,1)
            xt += theta*gamma + sigma*np.sqrt(gamma)*z

            Tj = dt*(j+1)
            lnst = lns0 + (r-q+w)*Tj + xt

        price = np.exp(lnst)
        price_vec[i] = price
        
    return price_vec