from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt

df_price = data.get_data_yahoo(['XLB', 'XLF', 'XLK', 'XLP', 'XLV'], start='2000-03-01', end='2021-02-28')['Adj Close']
df_ret = np.log(df_price/df_price.shift(1)).dropna()
ret = np.array(df_ret.mean()*252)  # convert to annualized return
cov_mat = np.array(df_ret.cov()*252)  # convert to annualized covariance
plot_efficient_frontier(ret, cov_mat)