import numpy as np
import pandas as pd
import math

from arch import arch_model
from pandas_datareader import data
from scipy.stats import norm
from scipy.optimize import minimize, Bounds, LinearConstraint

df_px = data.get_data_yahoo(('SPY'), start='2000-03-01', end='2021-02-28').loc[:, 'Adj Close']
df_rets = df_px.pct_change(1).dropna()
df_rets

alpha = 0.2
beta = 0.2
gamma = 0.25
sigma_0 = 0.1

#calculate GARCH coefficients using Maximum Likelihood
def garchLogLikelihood(params, df_rets):
    alpha = params[0]
    beta = params[1]
    gamma = params[2]
    sigma_0 = params[3]
    
    logLikeli = -len(df_rets)*np.log(math.sqrt(2*math.pi))
    sigma_i = sigma_0
    ret_i = df_rets[0]
    for ii in range(2, len(df_rets)):
        sigma_i = alpha + beta * ret_i + gamma * sigma_i
        ret_i = df_rets[ii]

        logLikeli -= (0.5 * np.log(sigma_i**2) + 0.5*(ret_i**2/sigma_i**2))
    
    return -logLikeli

res = minimize(garchLogLikelihood,
               x0 = [alpha, beta, gamma, sigma_0],
               bounds  = ((0.0, None),(0.0, None), (0.0, None), (0.0, None)),
         	   args = (df_rets), 
         	   tol = 1e-12,
         	   method = 'SLSQP',
         	   options={'maxiter': 2500, 'ftol': 1e-14})

print(res.message)
print(res['x'])

#calculate GARCH coefficients using arch package
garch = arch_model(df_rets, vol='GARCH', p=1, q=1)
garch_fitted = garch.fit()
print(garch_fitted)