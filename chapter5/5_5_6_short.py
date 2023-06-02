prices = data.get_data_yahoo('SPY', start='2000-03-01', end='2021-02-28').loc[:, 'Adj Close']
rets = prices.pct_change(1)
adf, pvalue, usedlag, nobs, critical_values, icbest = adfuller(prices) #check the price series for stationarity
arma = ARIMA(rets.to_numpy(), order=(1, 0, 0)).fit() #check whether the returns follow an AR(1) process
arma.summary()