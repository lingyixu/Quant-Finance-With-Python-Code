from pyfinance.options import BSM

def bs_sabr_vol(F_0, K, T, sigma_0, beta, alpha, rho): 
    normVol = sabr_normal_vol(F_0,strike,T,beta,sigma_0,alpha,rho)
    normPx = bachelier_call(F_0,strike,T,normVol,0.0)
    impVol = get_implied_vol_bs(F_0,strike,T,0.0, normPx,0.2)
    return impVol

def strikeGivenDelta(F_0, T, rDom, rFor, delta, sigma):
    K = F_0 * math.exp(-sigma*np.sqrt(T)*norm.ppf(delta) + 0.5*(sigma**2)*T);
    return K
   
def sabrDeltForStrike(F_0, T, K, sigma_0, alpha, beta, rho, isPut):
    impVol = bs_sabr_vol(F_0, T, K, sigma_0, beta, alpha, rho)
    d1 = (1/(impVol*np.sqrt(T))) * ( np.log(F_0/K) + 0.5*(impVol**2)*T )

    if isPut > 0:
        delta = -norm.cdf(-d1)
    else:
        delta = norm.cdf(d1)
    return delta

def getStrikeGivenDeltaSABRSmile(F_0,T,sigma_0, alpha, beta, rho, isPut, deltaHat, initial_guess):
    root_fn = lambda x: sabrDeltForStrike(F_0,T,x,sigma_0, alpha, beta, rho, isPut) - deltaHat
    return root(root_fn,initial_guess)['x'][0]

def objectiveFunctionFX(params,beta,F_0,T, K_atm, K_c_st, K_p_st, rDom, rFor, sigma_atm, rr_vol, st_px):
    
    #extract the 25D risk reversal strikes
    K_c_rr = getStrikeGivenDeltaSABRSmile(F_0,T,params[0], params[1], beta, params[2], 0, 0.25, K_c_st)
    K_p_rr = getStrikeGivenDeltaSABRSmile(F_0,T,params[0], params[1], beta, params[2], 1, -0.25, K_p_st)
    
    #check the pricing error
    sigma_atm_hat = bs_sabr_vol(F_0, K_atm, T, params[0], beta, params[1], params[2])
    atm_error = (sigma_atm - sigma_atm_hat)**2
    
    sigma_rr_c_hat = bs_sabr_vol(F_0, K_c_rr, T, params[0], beta, params[1], params[2])
    sigma_rr_p_hat = bs_sabr_vol(F_0, K_p_rr, T, params[0], beta, params[1], params[2])
    rr_vol_hat = sigma_rr_c_hat - sigma_rr_p_hat
    rr_error = (rr_vol - rr_vol_hat)**2
    
    sigma_st_c_hat = bs_sabr_vol(F_0, K_c_st, T, params[0], beta, params[1], params[2])
    sigma_st_p_hat = bs_sabr_vol(F_0, K_p_st, T, params[0], beta, params[1], params[2])
    px_st_c_hat = math.exp(-r_d*T)*BSM(kind='call', S0=F_0, K = K_st_c, T = T, r = 0.00, sigma = sigma_atm+strangle_offset).value()
    px_st_p_hat = math.exp(-r_d*T)*BSM(kind='put', S0=F_0, K = K_st_p, T = T, r = 0.00, sigma = sigma_atm+strangle_offset).value()
    st_px_hat = (px_st_c_hat + px_st_p_hat)
    st_error = (st_px - st_px_hat)**2
    
    error = atm_error + rr_error + st_error
    return error

#input data
F_0, r_d, r_f, T = 100.0, 0.015, 0.005, 0.5
sigma_atm, sigma_rr, strangle_offset = 0.2, 0.04, 0.025

#extract the ATM  strike
K_atm = strikeGivenDelta(F_0, T, r_d, r_f, 0.5, sigma_atm)

#extract the 25D strangle strikes
K_st_c = strikeGivenDelta(F_0, T, r_d, r_f, 0.25, sigma_atm+strangle_offset)
K_st_p = strikeGivenDelta(F_0, T, r_d, r_f, 0.75, sigma_atm+strangle_offset)

#calculate 25D strangle price
st_c_px = math.exp(-r_d*T)*BSM(kind='call', S0=F_0, K = K_st_c, T = T, r = 0.00, sigma = sigma_atm+strangle_offset).value()
st_p_px = math.exp(-r_d*T)*BSM(kind='put', S0=F_0, K = K_st_p, T = T, r = 0.00, sigma = sigma_atm+strangle_offset).value()
st_px = st_c_px + st_p_px

results = minimize(objectiveFunctionFX,
               x0 = [0.15,0.5,0] ,
         	   bounds  = ((0.00001, F_0),(0.00001, 10),(-1,1)),
         	   args = (beta,F_0,T,K_atm, K_st_c, K_st_p, r_d, r_f, sigma_atm, sigma_rr, st_px), 
         	   tol = 1e-14,
         	   method = 'SLSQP',
         	   options={'maxiter': 400, 'ftol': 1e-14})['x']

print(f'sigma_0 = {results[0]} \nalpha = {results[1]} \nrho = {results[2]}')