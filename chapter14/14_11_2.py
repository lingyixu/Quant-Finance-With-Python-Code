from scipy.stats import norm
from scipy.optimize import minimize, Bounds, LinearConstraint

def solveForSigmaAssetsAndValueOfEquity(params, A, L, sigmaEq, t, r):
        sigmaAssetsHat = params[0]
        EHat = params[1]
        
        d1 = (math.log(A/L) + r + 0.5*sigmaAssetsHat**2*t)/(sigmaAssetsHat * math.sqrt(t))
        d2 = (math.log(A/L) + r - 0.5*sigmaAssetsHat**2*t)/(sigmaAssetsHat * math.sqrt(t))
    
        sigmaAssetsError = (sigmaAssetsHat - sigmaEq * norm.cdf(d1) * (EHat / A))**2
        eError = (EHat - (A * norm.cdf(d1) - L * math.exp(-r*t) * norm.cdf(d2)))**2
        
        return (sigmaAssetsError + eError)

A = 100.0
L = 90.0
sigmaEq = 0.5
t = 5.0
r = 0.0

bounds = Bounds((0,0), (None, None))
guess = (sigmaEq, A - L)
guess
res = minimize(solveForSigmaAssetsAndValueOfEquity,
               x0 = guess,
               bounds  = ((0.0, None),(0.0, None)),
         	   args = (A, L, sigmaEq, t, r), 
         	   tol = 1e-10,
         	   method = 'SLSQP',
         	   options={'maxiter': 400, 'ftol': 1e-14})['x']

print(res)
print(solveForSigmaAssetsAndValueOfEquity(res, A, L, sigmaEq, t, r))

def merton_model(A, L, sigmaAssets, t, r):

    d1 = (math.log(A/L) + r + 0.5*sigmaAssets**2*t)/(sigmaAssets * math.sqrt(t))
    d2 = (math.log(A/L) + r - 0.5*sigmaAssets**2*t)/(sigmaAssets * math.sqrt(t))

    E = A * norm.cdf(d1) - L * math.exp(-r*t) * norm.cdf(d2)
    
    DD = (math.log(A/L) + (r - 0.5*sigmaAssets**2*t)) / (sigmaAssets * math.sqrt(t))
    pdef = norm.cdf(DD)
    return E, sigmaAssets, DD, pdef

print(merton_model(A, L, res[0], t, r))