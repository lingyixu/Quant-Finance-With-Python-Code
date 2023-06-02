import numpy as np

ret_aapl = np.random.random(size=200)
ret_spy = np.random.random(size=200)

# calculate the covariance matrix using np.cov()
print(np.cov(ret_aapl, ret_spy))

# calculate the correlation matrix using np.corrcoef()
print(np.corrcoef(ret_aapl, ret_spy))