# Coding Example: Regularization Models

from sklearn.linear_model import Ridge, Lasso
import numpy as np

np.random.seed(0)
x = np.linspace(0, 10, 20)
epsilon = np.random.randn(20)
y = 3 * x + epsilon

ridge = Ridge(alpha=0.1)
ridge.fit(x[:, np.newaxis], y)
print(ridge.coef_, ridge.intercept_)  # [2.88471143] 1.1457774515537391

lasso = Lasso(alpha=0.1)
lasso.fit(x[:, np.newaxis], y)
print(lasso.coef_, lasso.intercept_)  # [2.87542027] 1.1922332348198434
