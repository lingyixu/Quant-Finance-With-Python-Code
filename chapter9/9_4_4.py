from scipy.optimize import root

def bs_call(S_0,K,T,sigma,r):
    d_1 = (np.log(S_0/K) + T*(r + (sigma**2)/2))/(sigma*np.sqrt(T))
    d_2 = d_1 - sigma*np.sqrt(T)
    return S_0*norm.cdf(d_1) - K*np.exp(-r*T)*norm.cdf(d_2)

def get_implied_vol_bs(S_0,K,T,r,observed_px, initial_guess):
    root_fn = lambda x: bs_call(S_0,K,T,x,r) - observed_px
    return root(root_fn,initial_guess)['x'][0]