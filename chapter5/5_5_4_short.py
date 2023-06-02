Xs = np.random.rand(240, 1)  # stock returns
Ys = np.random.rand(240, 3)  # Fama-French 3 factors' returns

regr = linear_model.LinearRegression()
regr.fit(Xs, Ys)
Ys_pred = regr.predict(Xs)
print('Coefficients: \n', regr.coef_)