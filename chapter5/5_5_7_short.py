rets = np.random.random(100)
arma = ARIMA(rets.to_numpy(), order=(1, 0, 1)).fit()