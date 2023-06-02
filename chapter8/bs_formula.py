import numpy as np
from scipy.stats import norm

def bs_call(S_0,K,T,sigma,r):
    d_1 = (np.log(S_0/K) + T*(r + (sigma**2)/2))/(sigma*np.sqrt(T))
    d_2 = d_1 - sigma*np.sqrt(T)
    return S_0*norm.cdf(d_1) - K*np.exp(-r*T)*norm.cdf(d_2)

print(bs_call(S_0 = 100, K = 105, T = 0.5, sigma = 0.3, r = 0.02))
#6.779490734346545