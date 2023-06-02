# Implied Volatility Premium in Practice: S&P 500
import numpy as np
import pandas as pd

spy_close = pd.read_csv('SPY.csv', index_col=0, parse_dates=True)['Adj Close']
spy_ret = (np.log(spy_close) - np.log(spy_close.shift(1))).dropna()
vix_close = pd.read_csv('VIX.csv', index_col=0, parse_dates=True)['Adj Close']

real_vol = spy_ret.rolling(window=30).std() * np.sqrt(252)
implied_vol = vix_close / 100
premium = implied_vol - real_vol
premium.describe()
# count    221.000000
# mean       0.029574
# std        0.134173
# min       -0.436174
# 25%        0.019543
# 50%        0.062005
# 75%        0.104271
# max        0.243735
