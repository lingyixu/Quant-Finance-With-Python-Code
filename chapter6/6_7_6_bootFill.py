import yfinance
import random

df_price = yfinance.download(['SPY', 'AAPL', 'GOOG'], start='2020-03-01', end='2021-02-28')['Adj Close']
df_ret = df_price.pct_change().dropna()
N = df_ret.shape[0]
m = 10    # length of the missing data period
boot_index = random.sample(range(N), m)
df_boot = df_ret.iloc[boot_index].set_index(pd.date_range(start='2021-03-01', end='2021-03-12', freq='B'))
