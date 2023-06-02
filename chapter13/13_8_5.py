def asymptotic_normal_vol(T,K,F0,sigma0,alpha,beta,rho):
    
    Fmid = (F0 + K)/2
    zeta = alpha/(sigma0 * (1-beta)) * (F0 ** (1-beta) - K **(1-beta))
    eps = T*alpha**2
    delta = np.log((np.sqrt(1-2 * rho * zeta + zeta**2) + zeta - rho)/(1-rho))
    gamma1 = beta/Fmid
    gamma2 = beta * (beta -1)/Fmid**2
    
    parta = alpha * (F0-K)/delta
    partb1 = (2*gamma2 - gamma1**2)/24 * (sigma0 * Fmid ** beta /alpha)**2
    partb2 = rho * gamma1/4 * sigma0 * Fmid **beta/alpha
    partb3 = (2-3 *rho **2)/24
    partb = (1+(partb1 + partb2 + partb3) * eps)
    
    return parta*partb

def rootfind_helper(sabr_params,T,K_list,F0,sigma_list):
    
    sigma0,alpha,rho = sabr_params
    beta = 0.5
    MSE = 0
    
    for i in range(len(K_list)):
        
        diff = asymptotic_normal_vol(T,K_list[i],F0,sigma0,alpha,beta,rho) - sigma_list[i]
        
        MSE += diff**2
        
    return MSE

def calibrate_sabr(T_list,K_table,F0_list,sigma_table):
    
    init_guess = [0.1,0.1,-0.1]
    
    params = np.zeros((len(T_list,3)))
    
    for T,i in enumerate(T_list):
        
        
        opt = scipy.minimize(rootfind_helper,init_guess,args = (T,K_table[i], F0_list[i],sigma_table[i]), method = 'SLSQP', bounds = ((0.01,1.5),(0,1.5),(-1,1)))
        params[i] = opt.x
    
    return params