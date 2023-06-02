def heston_simu(S0, K, r, T, v0, sig, k, theta, rho, n, N):
    
    dt = T/N
    mean = (0,0)
    cov = [[dt,rho*dt],[rho*dt,dt]]
    st_vec = np.empty(n)
    vt_vec = np.empty(n)
    payoff_vec = np.empty(n)
    price_vec = np.empty(n)

    for i in range(n):
    
        x = np.random.multivariate_normal(mean,cov,(N,1))
        st = S0
        vt = v0
    
        for j in range(N):
            dst = r*st*dt + np.sqrt(vt)*st*x[j][0][0]
            dvt = k*(theta-vt)*dt + sig*np.sqrt(vt)*x[j][0][1]
            st += dst
            vt += dvt
            if vt<0:
                vt = -vt
    
        payoff_vec[i] = max(st-K,0)
        price_vec[i] = payoff_vec[i]*np.exp(-r*T)
        st_vec[i] = st
        vt_vec[i] = vt
        
    plt.hist(st_vec,bins=100)
    plt.title("Terminal stock price distribution")
    plt.xlabel("stock price")
    plt.ylabel("frequncy per " + str(n) + " trials")
    plt.show()

    return price_vec
