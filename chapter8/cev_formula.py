from scipy.stats import ncx2

def cev_call(S_0,K,T,sigma,beta,r):
    v = 1/(2*(1-beta))
    x_1 = 4*(v**2)*(K**(1/v))/((sigma**2) * T)
    x_2 = 4*(v**2)*((S_0*np.exp(r*T))**(1/v))/((sigma**2) * T)
    kappa_1 = 2*v + 2
    kappa_2 = 2*v
    lambda_1 = x_2
    lambda_2 = x_1
    return np.exp(-r*T)*((S_0*np.exp(r*T)*(1-ncx2.cdf(x_1,kappa_1,lambda_1))) - K*ncx2.cdf(x_2,kappa_2,lambda_2))

print(cev_call(S_0 = 100, K = 100, T = 0.5, sigma =4, r = 0.02, beta  = 0.5))
#11.676110446148732