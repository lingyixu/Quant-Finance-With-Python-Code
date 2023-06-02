import numpy as np
import pandas as pd
import math
from scipy.stats import norm

#Define the base class
class StochasticProcess:
	def __init__(self, tau=1.0, S0=100.0, strike=100.0, rf=0.0, div=0.0):
		self.T = tau
		self.S = S0
		self.K = strike
		self.r = rf
		self.q = div

	def price(self):
		print("method not defined for base class")        

#Define the derived class
class BlackScholesProcess(StochasticProcess):
	def __init__(self, sig=0.1, tau=1.0, S0=100.0, strike=100.0, rf=0.0, div=0.0):
		self.sigma = sig
		StochasticProcess.__init__(self, tau, S0, strike, rf, div)

	def price(self):
		sigmaRtT = (self.sigma * math.sqrt(self.T))
		rSigTerm = (self.r + self.sigma * self.sigma/2.0) * self.T
		d1 = (math.log(self.S/self.K) + rSigTerm) / sigmaRtT
		d2 = d1 - sigmaRtT
		term1 = self.S * norm.cdf(d1)
		term2 = self.K * math.exp(-self.r * self.T) * norm.cdf(d2)
		return  term1 - term2 

bsProcess = BlackScholesProcess(0.1)
px = bsProcess.price()
