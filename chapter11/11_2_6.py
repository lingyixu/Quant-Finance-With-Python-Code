# Black-Scholes Theta
import numpy as np
from scipy.stats import norm

s0, K, r, T, sigma = 100, 100, 0.05, 1, 0.2
d1 = (np.log(s0/K) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
theta_c = -s0*norm.pdf(d1)*sigma / (2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2)  # -6.414027546438197
theta_p = -s0*norm.pdf(d1)*sigma / (2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2)  # -1.657880423934626
