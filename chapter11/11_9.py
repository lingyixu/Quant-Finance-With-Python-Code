# Delta and Gamma in Practice: Delta and Gamma By Moneyness
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import pandas as pd
from pathlib import Path
fig_path = Path(__file__).parent.parent / 'figures'
plt.style.use('grayscale')

x = np.arange(0, 200, 1)
k = 100
h = 10

s = x
c_k = np.maximum(s - k, 0)
p_k = np.maximum(k - s, 0)
c_kph = np.maximum(s - (k + h), 0)
c_kp2h = np.maximum(s - (k + 2*h), 0)
c_kmh = np.maximum(s - (k - h), 0)
p_kph = np.maximum((k + h) - s, 0)
p_kmh = np.maximum((k - h) - s, 0)

# covered call
payoff_covered_c = s - c_k
plt.figure(figsize=(12, 8))
plt.title("Payoff of Covered Calls")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_covered_c)
plt.savefig(fig_path / 'payoff_covered_calls.png')

# call spread 
payoff_call_spread = c_k - c_kph
plt.figure(figsize=(12, 8))
plt.title("Payoff of Call Spread ")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_call_spread)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_call_spread.png')

# put spread 
payoff_put_spread = p_k - p_kmh
plt.figure(figsize=(12, 8))
plt.title("Payoff of Put Spread")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_put_spread)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_put_spread.png')

# straddles 
payoff_staddles = p_k + c_k
plt.figure(figsize=(12, 8))
plt.title("Payoff of Straddles")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_staddles)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_staddles.png')

# strangles 
payoff_strangles = p_kmh + c_kph
plt.figure(figsize=(12, 8))
plt.title("Payoff of Strangles")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_strangles)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_strangles.png')

# butterflies 
payoff_butterflies = c_kph - 2*c_k + c_kmh
plt.figure(figsize=(12, 8))
plt.title("Payoff of Butterflies")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_butterflies)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_butterflies.png')

# condor
payoff_condor = c_kmh - c_k - c_kph + c_kp2h
plt.figure(figsize=(12, 8))
plt.title("Payoff of Condor")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_condor)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_condor.png')

# canlender spread
k, r, sigma, T = 100, 0.0, 0.25, 1
d1 = (np.log(s/k) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
c = s * norm.cdf(d1) - k * np.exp(-r * T) * norm.cdf(d2)
payoff_calender_spread = c - c_k
plt.figure(figsize=(12, 8))
plt.title("Payoff of Calender Spread")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_calender_spread)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_calender_spread.png')

# risk reversal
delta, s0 = 0.1, 100
k_c = s0 / np.exp(norm.ppf(delta) * (sigma * np.sqrt(T)) - (r + 0.5*sigma**2) * T)
k_p = s0 / np.exp(-norm.ppf(delta) * (sigma * np.sqrt(T)) - (r + 0.5*sigma**2) * T)
c = np.maximum(s - k_c, 0)
p = np.maximum(k_p - s, 0)
payoff_risk_reversal = c - p
plt.figure(figsize=(12, 8))
plt.title("Payoff of Risk Reversal")
plt.xlabel("Asset Price")
plt.ylabel("Payoff")
plt.plot(x, payoff_risk_reversal)
plt.hlines(0, x[0], x[-1], linestyles='dashed')
plt.savefig(fig_path / 'payoff_risk_reversal.png')

