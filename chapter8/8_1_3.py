import statsmodels.api as sm

spy_prices = dt('SPY',data_source='yahoo',start = '2015-01-01',end = '2021-01-01')['Adj Close']
spy_returns = spy_prices.pct_change(1).dropna() 
log_returns = np.log(1+spy_returns) 

#compare log-returns to normal distribution
fig, ax = plt.subplots(figsize = (12,8))
sm.qqplot(log_returns, norm, fit=True, line="45",ax =ax)
plt.title("Comparison of log-returns to normal distribution")
plt.show()

#equivalently compare returns to lognormal
fig, ax = plt.subplots(figsize = (12,8))
sm.qqplot(spy_returns, lognorm, fit=True, line="45", ax =ax)
plt.title("Comparison of returns to log-normal distribution")
plt.show()