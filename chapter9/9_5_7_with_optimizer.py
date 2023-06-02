from scipy.optimize import minimize

#the function we are minimizing
def portfolio_variance(weights,cov_mat):
    return weights.T@cov_mat@weights

def min_var_portfolio_opt(cov_mat):
    guess = np.array([1/len(cov_mat)]*len(cov_mat)).reshape(-1,1) #equal weights guess
    cons = {'type': 'eq', 'fun': lambda x:  np.sum(x)-1} #sum of weights equal to 1 
    return minimize(portfolio_variance,x0=guess,args=(cov_mat),constraints=cons,tol=1e-8, method = 'SLSQP')['x']

correlation = -0.4
sigma_1 = 0.25
sigma_2 = 0.3
cov_mat = np.array([[sigma_1**2,correlation*sigma_1*sigma_2],[correlation*sigma_1*sigma_2,sigma_2**2]])

min_var_portfolio_opt(cov_mat)

#array([0.56470588, 0.43529412])