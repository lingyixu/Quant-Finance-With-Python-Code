import numpy as np
import math
from scipy.optimize import minimize, Bounds, LinearConstraint

def getSurvProbAtT(T, cdsTenors, cdsLambdas, recov):
    survProb = 1.0
    prevT = 0.0
    for tenor_ii, lambda_ii in zip(cdsTenors, cdsLambdas):
        if (T > prevT):
            tau = min(tenor_ii, T) - prevT
            survProb *= math.exp(-tau * lambda_ii)
        prevT = tenor_ii
        
    return survProb

def pvCDS(cdsLambdas, cdsTenors, cdsSpread, cdsMat, coupon_frequency, rf, recov):
    total_payments = coupon_frequency * cdsMat
    pv_def_leg = 0.0
    pv_no_def_leg = 0.0
    
    for payment in range(1,total_payments+1):
        payment_time = payment/coupon_frequency
        
        pv_no_def_leg += cdsSpread * math.exp(-rf * payment_time) * getSurvProbAtT(payment_time, cdsTenors, cdsLambdas, recov)
        
        lambda_ord = np.where(cdsTenors == min(cdsTenors[cdsTenors >= payment_time]))[0][0]
        lambda_curr = cdsLambdas[lambda_ord]
        
        pv_def_leg +=  (1 - recov) * math.exp(-rf * payment_time) * getSurvProbAtT(payment_time, cdsTenors, cdsLambdas, recov) * lambda_curr
               
    return pv_def_leg, pv_no_def_leg

def cdsPricingErrorSquared(cdsLambdas, cdsTenors, cdsSpreads, coupon_frequency, rf, recov):
    sse = 0.0
    
    for tenor_ii, spread_ii in zip(cdsTenors, cdsSpreads):
        pv_def_leg_ii, pv_no_def_leg_ii = pvCDS(cdsLambdas, cdsTenors, spread_ii, tenor_ii, coupon_frequency, rf, recov)
        pv_cds_ii = (pv_def_leg_ii - pv_no_def_leg_ii)
        sse += pv_cds_ii**2
        
    return sse;

cdsSpreads = np.asarray([120, 135, 150, 160, 175]) / 10000.0
cdsTenors = np.asarray([1, 3, 5, 7, 10])
cdsLambdas = [0.05, 0.05, 0.05, 0.05, 0.05]
coupon_frequency = 2
rf = 0.005
recov = 0.4

pvCDS(cdsLambdas, cdsTenors, 0.05*(1-0.4), 5, 2, 0.0, 0.4)

res = minimize(cdsPricingErrorSquared,
               x0 = cdsLambdas,
               bounds  = ((0.0, None),(0.0, None), (0.0, None), (0.0, None), (0.0, None)),
         	   args = (cdsTenors, cdsSpreads, coupon_frequency, rf, recov), 
         	   tol = 1e-12,
         	   method = 'SLSQP',
         	   options={'maxiter': 2500, 'ftol': 1e-14})

res