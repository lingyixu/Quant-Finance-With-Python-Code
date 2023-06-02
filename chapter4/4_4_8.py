import math
from scipy.stats import norm

def callPx(s_0, k, r, sigma, tau):
	sigmaRtT = (sigma * math.sqrt(tau))
	rSigTerm = (r + sigma * sigma/2.0) * tau
	d1 = (math.log(s_0/k) + rSigTerm) / sigmaRtT
	d2 = d1 - sigmaRtT
	term1 = s_0 * norm.cdf(d1)
	term2 = k * math.exp(-r * tau) * norm.cdf(d2)
	price = term1 - term2
	return  price 

px = callPx(100, 100, 0.0, 0.1, 0.25)
print(px)