import numpy as np
from scipy.stats import norm

def bachelier_call(S_0,K,T,sigma,r):
    d_plus = (S_0*np.exp(r*T) - K)/(sigma*np.sqrt(T))
    return np.exp(-r*T)*sigma*np.sqrt(T)*(d_plus*norm.cdf(d_plus) + norm.pdf(d_plus))

print(bachelier_call(S_0 = 100, K = 105, T = 0.5, sigma = 30, r = 0.02))
#6.549163351317259