from pandas_datareader import DataReader

prices = DataReader(['SPY','AGG'],'yahoo','2018-01-01','2021-01-01')['Adj Close']
returns = prices.pct_change().dropna()

corr = returns.corr().iloc[0,1] #taking the off diagonal term of the matrix
sigma_1, sigma_2 = returns.std()

min_var_portfolio(sigma_1,sigma_2,corr)
#(0.040936160470639964, 0.95906383952936)