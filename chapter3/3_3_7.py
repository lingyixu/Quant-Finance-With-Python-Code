import numpy as np

Xs = np.concatenate((np.full((100, 1), 1), np.random.rand(100, 10)), axis=1) 
Ys = np.random.rand(100, 1)

# OLS Betas
betas = np.linalg.inv(Xs.T @ Xs) @ Xs.T @ Ys
print(betas)