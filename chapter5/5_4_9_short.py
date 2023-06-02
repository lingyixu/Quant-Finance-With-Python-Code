from pandas_datareader import data
df_px = data.get_data_yahoo('SPY', start='2020-03-01', end='2021-02-28').loc[:, 'Adj Close']
df_rets = df_px.pct_change() # simple returns
df_log_rets = np.log(df_px / df_px.shift(1)) #log returns

df_rets.count()             # count
df_rets.mean()              # mean
df_rets.rolling(10).mean()  # rolling mean

df_rets.median()            # median
df_rets.quantile(q=0.75)    # quantile

df_rets.std()               # standard deviation
df_rets.rolling(10).std()   # rolling standard deviation