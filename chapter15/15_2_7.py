import math

def fxBsCall(S0, K ,sigma, r_d, r_f, T):
    F = S0 * exp ((r_d - r_f) * T)
    d1 = (1/(sigma*np.sqrt(T))) * ( np.log(F/K) + 0.5*(sigma**2)*T )
    d2 = d1 -sigma*np.sqrt(T)
    pxCall = np.exp(-r*T)*( F*norm.cdf(d1) - K*norm.cdf(d2) )
    return pxCall