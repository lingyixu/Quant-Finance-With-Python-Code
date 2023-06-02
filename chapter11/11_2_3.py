# Calculating Delta and Gamma
import numpy as np
from scipy.stats import norm

s0, K, r, T, sigma = 100, 100, 0.05, 1, 0.2
d1 = (np.log(s0/K) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
delta_c = norm.cdf(d1)  # 0.6368306511756191
delta_p = -norm.cdf(-d1)  # -0.3631693488243809
