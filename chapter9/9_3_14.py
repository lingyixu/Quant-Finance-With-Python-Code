def heston_characteristic_eqn(u, sigma, k,p,s_0,r,t,theta, v_0):
    lambd = np.sqrt((sigma**2)*((u**2)+1j*u) + (k - 1j*p*sigma*u)**2) 
    omega_numerator = np.exp(1j*u*np.log(s_0)+1j*u*(r)*t+(1/(sigma**2))*k*theta*t*(k - 1j*p*sigma*u))
    omega_denominator = (np.cosh(0.5*lambd*t) + (1/lambd)*(k - 1j*p*sigma*u)*np.sinh(0.5*lambd*t))**((2*k*theta)/(sigma**2))
    phi = (omega_numerator/omega_denominator) * np.exp(-((u**2 + 1j*u)*v_0)/(lambd*(1/np.tanh(0.5*lambd*t)) + (k - 1j*p*sigma*u)))
    return phi

def calc_fft_heston_call_prices(alpha, N, delta_v, sigma, k, p, s_0, r, t, theta, v_0, K = None):
    #delta is the indicator function
    delta = np.zeros(N)
    delta[0] = 1 
    delta_k = (2*np.pi)/(N*delta_v)
    if K == None:
        #middle strike is at the money
        beta = np.log(s_0) - delta_k*N*0.5 
    else:
        #middle strike is K
        beta = np.log(K) - delta_k*N*0.5
    k_list = np.array([(beta +(i-1)*delta_k) for i in range(1,N+1) ])
    v_list = np.arange(N) * delta_v
    #building fft input vector
    x_numerator = np.array( [((2-delta[i])*delta_v)*np.exp(-r*t)  for i in range(N)] )
    x_denominator = np.array( [2 * (alpha + 1j*i) * (alpha + 1j*i + 1) for i in v_list] )
    x_exp = np.array( [np.exp(-1j*(beta)*i) for i in v_list] )
    x_list = (x_numerator/x_denominator)*x_exp* np.array([heston_characteristic_eqn(i - 1j*(alpha+1),sigma, k,p,s_0,r,t,theta, v_0) for i in v_list])
    #fft output
    y_list = np.fft.fft(x_list)
    #recovering prices
    prices = np.array( [(1/np.pi) * np.exp(-alpha*(beta +(i-1)*delta_k)) * np.real(y_list[i-1]) for i in range(1,N+1)] )
    return prices, np.exp(k_list)