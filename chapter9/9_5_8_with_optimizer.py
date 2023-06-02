from pandas_datareader import DataReader

prices = DataReader(['SPY','AGG'],'yahoo','2018-01-01','2021-01-01')['Adj Close']
returns = prices.pct_change().dropna()
cov_mat = returns.cov()

min_var_portfolio_opt(cov_mat)
#array([0.04093615, 0.95906385])