'''
13_8_6
'''

import pandas as pd
import numpy as np
import math
import scipy.optimize as optimize
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use('grayscale')
pd.options.mode.chained_assignment = None  # default='warn'
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



def calc_disc(s,t,f_s):
    integral = math.exp(-(t-s)*f_s)
    return integral 


def calc_for(s,t,f_s):
    integral = math.exp((t-s)*f_s)
    for_r = (1/(t-s))*(integral -1)
    return for_r

def calc_disc(s,t,f_s):
    return math.exp(-(t-s)*f_s)


def calc_swap(s,t,f_s):
    
    numerator = 0
    denominator = 0
    
    for i in range(t-s):
        numerator += calc_for(s+i,s+i+1,f_s)*calc_disc(s,s+i,f_s)
        denominator += calc_disc(s,s+i,f_s)
        
    return numerator/denominator


def root_swap(f_s,s,t,swap_given):
    
    return calc_swap(s,t,f_s) - swap_given

def calc_annuity(s,t,f_s):
    
    annu = 0
    for i in range(s+1,t+1,1):
        annu += calc_disc(s,i,f_s)

    
    return calc_disc(0,s,f_s)*annu

def calc_black_delta(sigma, annu, s,f0,strike,f_s):
    dised_num = annu
    d1 = (np.log(f0/strike) + 0.5*sigma**2*s)/(sigma*np.sqrt(s))
    d2 = (np.log(f0/strike) - 0.5*sigma**2*s)/(sigma*np.sqrt(s))
    
    delta = norm.cdf(d1)
    
    return delta
        
def black_swap(sigma, annu, s,f0,strike,f_s,price_given):
    dised_num = annu
    d1 = (np.log(f0/strike) + 0.5*sigma**2*s)/(sigma*np.sqrt(s))
    d2 = (np.log(f0/strike) - 0.5*sigma**2*s)/(sigma*np.sqrt(s))
    
    price = dised_num*(f0*norm.cdf(d1) - strike*norm.cdf(d2))
    
    return price-price_given
    
def bach_swap(annu,sigma,s,f0,strike,f_s):
    dised_num = annu 
    d1 = (f0-strike)/(sigma*np.sqrt(s))
    d2 = -d1
 
    P = dised_num * sigma*np.sqrt(s) *(d1 * norm.cdf(d1) + norm.pdf(d1))
    return P


def make_delta(K,F0,sigma_0,alpha,beta,rho):
    xi = (alpha/(sigma_0*(1-beta)))*(F0**(1-beta) - K**(1-beta))
    if( 1-2*rho*xi + xi**2< 0):
        print(rho,xi)
    
    num = np.sqrt(1-2*rho*xi + xi**2) + xi - rho
    denom = 1-rho
    
    delta = np.log(num/denom)
    
    return delta

def sabr_sig(T,K,F0,sigma_0,alpha,beta,rho):
    delta = make_delta(K,F0,sigma_0,alpha,beta,rho)
    
    Fmid = (F0 + K)/2
    CF = Fmid**beta
    
    h = 0.0001
    
    first_order_CF = ((Fmid+h)**beta - Fmid**beta)/h
    second_order_CF = ((Fmid+h)**beta - 2*CF + (Fmid-h)**beta)/(h**2)

    
    gamma1 = first_order_CF/CF
    gamma2 = second_order_CF/CF
    
    epsilon = T*alpha**2
    
    twoseven = (1+ ((2*gamma2 - gamma1**2)/24)*((sigma_0*CF)/alpha)**2 + ((rho*gamma1)/4)*((sigma_0*CF)/alpha) + (2-3*rho**2)/24)*epsilon
    
    result = alpha * ((F0-K)/delta)* twoseven
    return result

def sabr_helper(guess,T,strikes,F0,given_sigs):

    sigma_0 = guess[0]
    alpha = guess[1]
    rho = guess[2]
    beta = 0.5
    MSE = 0
    counter =0 
    for K in strikes:
        sabr_sigma = sabr_sig(T,K,F0,sigma_0,alpha,beta,rho)
        MSE += (sabr_sigma-given_sigs[counter])**2
        counter+=1

    return MSE




def main():
    
    
    swap_rates_bp = [117.45, 120.60, 133.03, 152.05, 171.85]
    expiries = [1,2,3,4,5]
    
    swap_rates_perc = [i/10000 for i in swap_rates_bp]
    
    
    bach_sig_df = pd.DataFrame()
    bach_sig_df['Expiry'] = expiries
    bach_sig_df['Tenor'] = [5,5,5,5,5]
    bach_sig_df['F0'] = swap_rates_bp
    bach_sig_df['ATM - 50'] = [57.31, 51.72, 46.29, 45.72, 44.92]
    bach_sig_df['ATM - 25'] = [51.51,46.87, 44.48, 41.80, 40.61]
    bach_sig_df['ATM - 5'] = [49.28, 43.09, 43.61, 38.92, 37.69]
    bach_sig_df['ATM + 5'] = [48.74, 42.63, 39.36, 38.19, 36.94]
    bach_sig_df['ATM + 25'] = [41.46, 38.23, 35.95, 34.41, 33.36]
    bach_sig_df['ATM + 50'] = [37.33, 34.55, 32.55, 31.15, 30.21]
    
    
    ###Calibrate SABR Params
    
    sabr_df = pd.DataFrame()
    sabr_df['Expiry'] = expiries
    sabr_df['Sigma_0'] = np.zeros(5)
    sabr_df['Alpha'] = np.zeros(5)
    sabr_df['Beta'] = np.zeros(5)
    sabr_df['Rho'] = np.zeros(5)
    sabr_df['MSE'] = np.zeros(5)
    
    
    init_guess = [0.03,0.4,-0.8 ]
    for i in range(len(expiries)):
        F_0 = swap_rates_perc[i]
        strikes_input = [F_0-50/10000, F_0-25/10000, F_0-5/10000, F_0+5/10000, F_0+25/10000, F_0+50/10000]
        given_sigs = bach_sig_df.iloc[i,3:].to_numpy()/10000
        sol = optimize.minimize(sabr_helper,init_guess,args = (i+1,strikes_input,F_0,given_sigs), tol = 0.0000001)
  
        params = sol.x
        sabr_df['Sigma_0'].iloc[i] = params[0]
        sabr_df['Alpha'].iloc[i] = params[1]
        sabr_df['Beta'].iloc[i] = 0.5
        sabr_df['Rho'].iloc[i] = params[2]
        sabr_df['MSE'].iloc[i] = sol.fun
        

    print("Sabr Params")
    print(sabr_df)
    
    sabr_vol_df= pd.DataFrame()
    sabr_vol_df['Expiry'] = expiries
    sabr_vol_df['Tenor'] = [5,5,5,5,5]
    sabr_vol_df['F0'] = swap_rates_bp
    sabr_vol_df['ATM - 50'] = np.zeros(5)
    sabr_vol_df['ATM - 25'] = np.zeros(5)
    sabr_vol_df['ATM - 5'] = np.zeros(5)
    sabr_vol_df['ATM + 5'] = np.zeros(5)
    sabr_vol_df['ATM + 25'] =np.zeros(5)
    sabr_vol_df['ATM + 50'] =np.zeros(5)
    
    for i in range(5):
        sigma_0 = sabr_df['Sigma_0'].iloc[i]
        alpha = sabr_df['Alpha'].iloc[i]
        beta = sabr_df['Beta'].iloc[i]
        rho = sabr_df['Rho'].iloc[i]
        ftest = swap_rates_perc[i]
        strikes_test = [ftest-50/10000, ftest-25/10000, ftest-5/10000, ftest+5/10000, ftest+25/10000, ftest+50/10000]
        for j in range(6):
            
            
            sabr_vol_test = sabr_sig(i+1,strikes_test[j],ftest,sigma_0,alpha,beta,rho)
            sabr_vol_df.iloc[i,j+3] = int(sabr_vol_test*1000000)/100
    
    print("Calibrated Sabr Volatilities")
    print(sabr_vol_df)
    
    plt.subplots(figsize = (15,10))
    plt.title('Calibrated SABR Normal Volatilities')
    plt.ylabel("Vol")
    plt.xlabel("Strike")
    
    for expiry_i in range(len(sabr_vol_df.index)):
        temp=[]
        for strike in range(3,9):
            temp.append(sabr_vol_df.iloc[expiry_i,strike])
            print(temp)
        
        plt.plot(['ATM - 50','ATM - 25','ATM - 5','ATM + 5','ATM + 25','ATM + 50'],temp, label =( "Expiry = " + str(sabr_vol_df['Expiry'].iloc[expiry_i]) +"Y"))
    plt.legend()

    
main()


