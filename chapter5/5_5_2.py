import numpy as np
from sklearn import datasets, linear_model

Xs = np.random.rand(100, 2)
Ys = np.random.rand(100, 1)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(Xs, Ys)
print(regr.coef_)
