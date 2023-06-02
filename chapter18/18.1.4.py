# Regularization Techniques in Practice: Impact on Expected Return Model
from pathlib import Path
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig_path = Path(__file__).parent.parent / 'figures'
plt.style.use('grayscale')


spy_close = pd.read_csv('SPY.csv', index_col=0, parse_dates=True)['Adj Close']
spy_ret = (np.log(spy_close) - np.log(spy_close.shift(1))).dropna()
y = spy_ret.to_numpy()[1:]  # y is t day return
x = spy_ret.shift(1).to_numpy()[1:]  # x is the t-1 dayreturn

ols = LinearRegression(fit_intercept=False)
ols.fit(x[:, np.newaxis], y)

alphas = np.linspace(0, 1, 10000)
ridge_coefs, lasso_coefs = [], []
for alpha in alphas:
    ridge = Ridge(alpha=alpha, fit_intercept=False)
    ridge.fit(x[:, np.newaxis], y)
    ridge_coefs.append(ridge.coef_[0])

    lasso = Lasso(alpha=alpha, fit_intercept=False)
    lasso.fit(x[:, np.newaxis], y)
    lasso_coefs.append(lasso.coef_[0])

plt.figure(figsize=(12, 8))
plt.title("Impact of Regularization")
plt.xlabel("Alpha")
plt.ylabel("Coefficient")
plt.plot(alphas, ridge_coefs)
plt.plot(alphas, lasso_coefs)
plt.hlines(ols.coef_[0], alphas[0], alphas[-1], linestyles='dashed')
plt.legend(['Ridge', 'Lasso', 'OLS'])
plt.savefig(fig_path / 'impact_on_expected_return_model.png')
