Xs = np.random.rand(100, 10)
Ys = np.random.rand(100, 1)

regr = linear_model.LinearRegression()
regr.fit(Xs, Ys)

# Make predictions
Ys_pred = regr.predict(Xs)

# The coefficients
regr.coef_