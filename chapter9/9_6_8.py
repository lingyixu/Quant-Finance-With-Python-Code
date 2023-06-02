from scipy.optimize import minimize

def sum_squares_cev(beta,S_0,sigma,r,call_prices, strikes, expiries):
    sum = 0
    for price, strike, expiry in zip(call_prices, strikes, expiries):
      sum += (price - cev_call(S_0,strike,expiry,sigma,r,beta))**2
    return sum

def find_beta_sigma_cev(S_0,r,call_prices, strikes, expiries, guess = [0.9,0.4],bounds = ((0.001,None),(0.001,None)),tol=1e-10):
    """
    call_prices, strikes, and expiries are arrays of equal length with each index corresponding to one option
    For example, if the first elements of each array are 10, 100, and 1 respectively, this corresponds to an option
    with price 10, strike 100, and 1 year to expiry
    """
    #first element is beta, second element is sigma
    unique_expiries = np.unique(expiries)
    calibrated_beta_sigma = {} #this is where the results will go for each expiry
    for expiry in unique_expiries:
      #how many times this expiry appears
      expiries_list = expiry*np.ones(np.sum(expiries == expiry)) 
      #where it appears
      indices = np.where(expiries == expiry)[0] 
      #what are the strikes for this expiry
      strikes_for_expiry = np.array(strikes)[indices] 
      #what are the market prices for this expiry
      prices_for_expiry = np.array(call_prices)[indices] 
      #the function to be minimized
      opt_func = lambda x: sum_squares_cev(x[0],S_0,x[1],r,prices_for_expiry, strikes_for_expiry, expiries_list) 
      #calibrated values
      beta, sigma = minimize(opt_func,guess, bounds = bounds ,method = 'SLSQP', tol=tol)['x'] 
      #saving the results
      calibrated_beta_sigma[expiry] = [beta, sigma]
    return calibrated_beta_sigma