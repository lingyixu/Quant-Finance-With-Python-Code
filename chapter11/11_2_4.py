# Delta and Gamma in Practice: Delta and Gamma By Moneyness
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import pandas as pd
from pathlib import Path
fig_path = Path(__file__).parent.parent / 'figures'
plt.style.use('grayscale')

df = pd.read_csv('AAPL_option_2023-06-15.csv', index_col=0)
c = df.loc[df['Contract Name'].str.contains('C')]
p = df.loc[df['Contract Name'].str.contains('P')]

s0 = 100  # close price of aapl on June 1 2021
sigma = 0.25  # estimate of annual volatility
T = 2  # roughly 2 years from now
r = 0.04  # 1 Yr Treasury Yield Curve Rates
K = range(50, 250)  # strike of call is identical to put in this case
d1 = (np.log(s0/K) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
delta_c = norm.cdf(d1)
delta_p = -norm.cdf(-d1)
gamma = norm.pdf(d1) / (s0 * sigma * np.sqrt(T))

plt.figure(figsize=(12, 8))
plt.title("Delta of Call Option")
plt.xlabel("Strike")
plt.ylabel("Delta")
plt.plot(K, delta_c)
plt.hlines(0, K.iloc[0], K.iloc[-1], linestyles='dashed')
plt.savefig(fig_path / 'call_delta.png')

plt.figure(figsize=(12, 8))
plt.title("Delta of Put Option")
plt.xlabel("Strike")
plt.ylabel("Delta")
plt.plot(K, delta_p)
plt.hlines(0, K.iloc[0], K.iloc[-1], linestyles='dashed')
plt.savefig(fig_path / 'put_delta.png')

plt.figure(figsize=(12, 8))
plt.title("Gamma of Call and Put Option")
plt.xlabel("Strike")
plt.ylabel("Gamma")
plt.plot(K, gamma)
plt.savefig(fig_path / 'call_put_gamma.png')
