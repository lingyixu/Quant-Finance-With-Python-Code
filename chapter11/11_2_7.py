# Delta and Gamma in Practice: Delta and Gamma By Moneyness
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import pandas as pd
from pathlib import Path
fig_path = Path(__file__).parent.parent / 'figures'
plt.style.use('grayscale')

option_files = ['AAPL_option_2021-06-03.csv', 'AAPL_option_2021-06-10.csv',
                'AAPL_option_2021-06-17.csv', 'AAPL_option_2021-06-24.csv',
                'AAPL_option_2021-07-01.csv', 'AAPL_option_2021-07-08.csv',
                'AAPL_option_2021-07-15.csv', 'AAPL_option_2021-08-19.csv',
                'AAPL_option_2021-09-16.csv', 'AAPL_option_2021-10-14.csv',
                'AAPL_option_2021-11-18.csv', 'AAPL_option_2021-12-16.csv',
                'AAPL_option_2022-01-20.csv', 'AAPL_option_2022-06-16.csv',
                'AAPL_option_2022-09-15.csv', 'AAPL_option_2023-01-19.csv',
                'AAPL_option_2023-03-16.csv', 'AAPL_option_2023-06-15.csv']
date_strs = [file.replace('AAPL_option_', '').replace('.csv', '') for file in option_files]
t = np.datetime64('2021-06-01')
T = np.array([np.datetime64(date_str) for date_str in date_strs])
s0 = 125  # close price of aapl on June 1 2021
K = 125  # at-the-money option
sigma = 0.25  # estimate of annual volatility
r = 0.04  # 1 Yr Treasury Yield Curve Rates

tau = (T - t).astype(int) / 365  # T-t in years
d1 = (np.log(s0/K) + (r + 0.5*sigma**2) * tau) / (sigma * np.sqrt(tau))
d2 = d1 - sigma * np.sqrt(tau)
theta_c = -s0*norm.pdf(d1)*sigma / (2*np.sqrt(tau)) - r*K*np.exp(-r*tau)*norm.cdf(d2)
theta_p = -s0*norm.pdf(d1)*sigma / (2*np.sqrt(tau)) + r*K*np.exp(-r*tau)*norm.cdf(-d2)

plt.figure(figsize=(12, 8))
plt.title("Theta of Call Option")
plt.xlabel("Time to Maturity")
plt.ylabel("Theta")
plt.plot(tau, theta_c)
plt.savefig(fig_path / 'call_theta.png')

plt.figure(figsize=(12, 8))
plt.title("Theta of Put Option")
plt.xlabel("Time to Maturity")
plt.ylabel("Theta")
plt.plot(tau, theta_p)
plt.savefig(fig_path / 'put_theta.png')
