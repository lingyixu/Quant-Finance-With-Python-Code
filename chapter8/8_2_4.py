def sabr_normal_vol(S_0,K,T,sigma_0,alpha,beta,rho):
    c = lambda x: x**beta
    c_prime = lambda x: beta*(x**(beta-1))
    c_prime_prime = lambda x: beta*(beta-1)*(x**(beta-2))
    S_mid = (S_0 + K)/2
    gamma_1 = c_prime(S_mid)/c(S_mid)
    gamma_2 = c_prime_prime(S_mid)/c(S_mid)
    zeta = alpha*(S_0**(1-beta) - K**(1-beta))/(sigma_0 * (1-beta))
    epsilon = T*(alpha**2)
    delta = np.log( (np.sqrt(1 - 2*rho*zeta + zeta**2) + zeta - rho)/(1-rho) )

    factor = alpha*(S_0 - K)/(delta)
    term_1 = ((2*gamma_2 - gamma_1**2)/24)* (sigma_0*c(S_mid)  / alpha)**2
    term_2 = rho*gamma_1*sigma_0*c(S_mid)/(4*alpha)
    term_3 = (2-3*(rho**2))/24
    return factor*(1 + epsilon*(term_1 + term_2 + term_3))

def sabr_call(S_0,K,T,sigma_0,r,alpha,beta,rho):
    assert(S_0 != K)
    vol = sabr_normal_vol(S_0,K,T,sigma_0,alpha,beta,rho)
    return bachelier_call(S_0,K,T,vol,r)